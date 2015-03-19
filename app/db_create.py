# db_create.py

import sqlite3
from config import DATABASE_PATH

with sqlite3.connect(DATABASE_PATH) as connection:
	#obtiene el cursor
	c = connection.cursor()

	#creamos la tabla
	c.execute("""CREATE TABLE tasks(task_id INTEGER PRIMARY KEY AUTOINCREMENT,
			name TEXT NOT NULL, due_date TEXT NOT NULL, 
			priority INTEGER NOT NULL, status INTEGER NOT NULL)""")

	#INSERTAMOS
	c.execute(
		'INSERT INTO tasks(name, due_date, priority, status)'
		'VALUES("Finish this Tutorial", "02/03/2015", 10, 1)'
	)
	c.execute(
		'INSERT INTO tasks(name, due_date, priority, status)'
		'VALUES("Finish real Python curso 2", "02/04/2015", 10, 1)'
	)