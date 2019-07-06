import os
import sqlite3

def make_tables(conn, schema_file='computing_schemata.sql'):
    with open(schema_file) as fd:
        lines = fd.readlines()
    statements = ''.join(lines).split(';')
    cursor = conn.cursor()
    for statement in statements:
        cursor.execute(statement)
    cursor.close()
    conn.commit()

def set_deliverables(conn, infile='deliverables.txt'):
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

def set_activities(conn, infile='activities.txt'):
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
        (3, 18, 1),
        (6, 18, 0),
        (8, 7, 1),
        (8, 15, 0),
        (8, 16, 0),
        (8, 17, 0),
        (8, 18, 1),
        (9, 3, 0),
        (9, 4, 1),
        (9, 5, 1),
        (9, 6, 1),
        (9, 7, 1),
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

if __name__ == '__main__':
    db_file = 'computing.sqlite3'
    os.remove(db_file)
    conn = sqlite3.connect(db_file)

    make_tables(conn)
    set_deliverables(conn)
    set_activities(conn)
    set_delivery_dependencies(conn)
    set_activity_dependencies(conn)

"""
CO Deliverables
* integration pipeline for end-to-end image generation
* workflow for extragalactic catalog generation
* interface improvements between image generation workflow components
* imsim improvements
* extragalactic catalog validation tools
* image simulation validation tools
* DM catalog validation tools
* Gen-3 butler version of DM processing pipeline
* Demonstrate ability to process 10% of Y1 LSST data at NERSC
* 5000 sq degree extragalactic catalog
* DC3 image simulations
* Final DC2 data products
* Final DC3 data prodcuts
* Commissioning simulation data products
* resource requirements for Y1 data access and analysis

External deliverables:
* Gen-3 Stack
* Gen-3 workflow implementation
* Performance-tuned Gen-3 Stack
* DC3 image simulation requirements
* Commissioning image simulation requirements

Activities
* DC3 image processing

"""
