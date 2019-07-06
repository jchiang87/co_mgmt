default:
	python fill_db_tables.py
	python computing_dag.py
	dot -Tpng computing_dag.dot > computing_dag.png
