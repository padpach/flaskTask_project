
from views import db
from datetime import datetime
from config import DATABASE_PATH
from flask.ext.sqlalchemy import SQLAlchemy

db.execute("""ALTER TABLE tasks RENAME TO old_tasks""")