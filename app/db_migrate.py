
from views import db
from datetime import datetime
from config import DATABASE_PATH
from flask.ext.sqlalchemy import SQLAlchemy
from models import User, Task

class migrar():

	def setUp(self):
		app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/task'
		return "Hola mundo"



if __name__ == "__main__":
	migrar()