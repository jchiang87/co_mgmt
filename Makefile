default:
	fill_db_tables.py
	computing_dag.py
	dot -Tpng computing_dag.dot > computing_dag.png
