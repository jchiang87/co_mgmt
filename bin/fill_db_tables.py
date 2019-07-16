#!/usr/bin/env python
import os
import sqlite3

from db_utils import *

db_file = 'computing.sqlite3'
if os.path.isfile(db_file):
    os.remove(db_file)
conn = sqlite3.connect(db_file)

make_tables(conn)
set_deliverables(conn)
set_activities(conn)
set_delivery_dependencies(conn)
set_activity_dependencies(conn)

