#!/usr/bin/env python
import sqlite3

class ComputingTables:
    def __init__(self, db_file='computing.sqlite3'):
        self.conn = sqlite3.connect('computing.sqlite3')

    def get(self, query):
        cursor = self.conn.cursor()
        cursor.execute(query)
        results = [tuple(_) for _ in cursor]
        cursor.close()
        return results

db_tables = ComputingTables()

output = open('computing_dag.dot', 'w')
output.write('digraph Computing_Workflow {\n')

# Write node shapes for computing group deliverables.
output.write('node [shape=box, color=black]; ')
query = '''select id, deliverableName from Deliverables
           where deliverableType="ComputingGroup"'''
co_deliverables = {int(key): "%d. %s" % (key, value) for key, value
                   in db_tables.get(query)}
output.write('; '.join(['"%s"' % _ for _ in co_deliverables.values()]) + '\n')

# Write node shapes for computing group deliverables.
output.write('node [shape=box, color=red]; ')
query = '''select id, deliverableName from Deliverables
           where deliverableType="External"'''
ext_deliverables = {int(key): "%d. %s" % (key, value) for key, value
                    in db_tables.get(query)}
output.write('; '.join(['"%s"' % _ for _ in ext_deliverables.values()]) + '\n')

deliverables = dict()
deliverables.update(co_deliverables)
deliverables.update(ext_deliverables)

# Write node shapes for activities.
output.write('node [shape=ellipse, color=black]; ')
query = 'select id, activityName from Activities'
activities = {int(key): "%d. %s" % (key, value) for key, value
              in db_tables.get(query)}
output.write('; '.join(['"%s"' % _ for _ in activities.values()]) + '\n')

# Write activity dependencies
query = 'select activityId, deliverableId, required from ActivityDependencies'
for activityId, deliverableId, required in db_tables.get(query):
    output.write('"%s" -> "%s"' % (deliverables[deliverableId],
                                   activities[activityId]))
    if required == 0:
        output.write(' [style=dashed];\n')
    else:
        output.write(';\n')

# Write deliverable dependencies
query = 'select deliverableId, activityId from DeliveryDependencies'
for deliverableId, activityId in db_tables.get(query):
    output.write('"%s" -> "%s";\n' % (activities[activityId],
                                      deliverables[deliverableId]))

output.write('}\n')
output.close()
