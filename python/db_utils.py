import os

__all__ = ['make_tables', 'set_deliverables', 'set_activities',
           'set_delivery_dependencies', 'set_activity_dependencies']

def make_tables(conn, schema_file=None):
    if schema_file is None:
        schema_file = os.path.join(os.environ['CO_MGMT_DIR'], 'data',
                                   'computing_schemata.sql')
    with open(schema_file) as fd:
        lines = fd.readlines()
    statements = ''.join(lines).split(';')
    cursor = conn.cursor()
    for statement in statements:
        cursor.execute(statement)
    cursor.close()
    conn.commit()

def set_deliverables(conn, infile=None):
    if infile is None:
        infile = os.path.join(os.environ['CO_MGMT_DIR'], 'data',
                              'deliverables.txt')
    values_list = []
    with open(infile) as fd:
        for line in fd:
            tokens = [_.strip() for _ in line.split(',')]
            tokens[0] = int(tokens[0])
            values_list.append(tokens)
    cursor = conn.cursor()
    for values in values_list:
        sql = '''INSERT INTO Deliverables
                 (id, deliverableName, deliveryDate, deliverableType)
                 VALUES (%d, "%s", "%s", "%s")''' % tuple(values)
        cursor.execute(sql)
    cursor.close()
    conn.commit()

def set_activities(conn, infile=None):
    if infile is None:
        infile = os.path.join(os.environ['CO_MGMT_DIR'], 'data',
                              'activities.txt')
    values_list = []
    with open(infile) as fd:
        for line in fd:
            tokens = [_.strip() for _ in line.strip().split(',')]
            tokens[0] = int(tokens[0])
            tokens[-1] = float(tokens[-1])
            values_list.append(tokens)
    cursor = conn.cursor()
    for values in values_list:
        sql = '''INSERT INTO Activities
                 (id, activityName, startDate, endDate, effortLevel)
                 VALUES (%d, "%s", "%s", "%s", %f)''' % tuple(values)
        cursor.execute(sql)
    cursor.close()
    conn.commit()

def set_delivery_dependencies(conn):
    values_list = [(1, 1),
                   (2, 3),
                   (3, 5),
                   (4, 2),
                   (5, 4),
                   (6, 6),
                   (7, 7),
                   (8, 8),
                   (9, 8),
                   (10, 3),
                   (11, 9),
                   (12, 10),
                   (13, 8),
                   (14, 11)
    ]
    cursor = conn.cursor()
    for values in values_list:
        sql = '''INSERT INTO DeliveryDependencies (deliverableId, activityId)
                 VALUES (%d, %d)''' % tuple(values)
        cursor.execute(sql)
    cursor.close()
    conn.commit()

def set_activity_dependencies(conn):
    values_list = [
        (1, 6, 0),
        (2, 1, 1),
        (2, 18, 1),
        (3, 5, 1),
        (3, 18, 1),
        (6, 18, 0),
        (8, 7, 1),
        (8, 15, 0),
        (8, 16, 0),
        (8, 17, 0),
        (8, 18, 1),
        (9, 3, 0),
        (9, 4, 1),
        (9, 6, 1),
        (9, 7, 1),
        (9, 10, 1),
        (9, 18, 1),
        (11, 11, 1),
        (11, 13, 1),
        (11, 8, 0),
        (11, 18, 1)
    ]
    cursor = conn.cursor()
    for values in values_list:
        sql = '''INSERT INTO ActivityDependencies
                 (activityId, deliverableId, required)
                 VALUES (%d, %d, %d)''' % tuple(values)
        cursor.execute(sql)
    cursor.close()
    conn.commit()
