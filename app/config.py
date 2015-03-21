#config.py

import os

#graba la ruta de la carpeta donde el script corre
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'flasktaskr.db'
CSRF_ENABLED = True
SECRET_KEY = 'my_precious'

# defines the la ruta de la  database
DATABASE_PATH = os.path.join(basedir, DATABASE)

# the database uri
#SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH
SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost/task'
