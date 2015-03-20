# db_create.py

from config import DATABASE_PATH
from views import db
from models import Task
from datetime import date



# Cremos la Base de Datos
db.create_all()

#insertamos
#db.session.add(Task("Finish this Tutorial", date(1015, 04, 01), 10, 1))
#db.session.add(Task("Terminar el Tuto 3", date(2014, 03, 13), 6, 1))
#db.session.add(Task("Love Life", date(2015, 05, 05), 6, 1))

#commit
db.session.commit()
	