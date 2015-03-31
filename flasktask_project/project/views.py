# project/views.py

#################
#### imports ####
#################


from project import app, db
from flask import flash, redirect, session, url_for
from functools import wraps


##########################
#### helper functions ####
##########################



def flash_errors(form):
	for field, errors in form.errors.items():
		for error in errors:
			flash(u"Error en el %s campo - %s" % (getattr(form, field).label.text, error), 'error')



def login_required(test):
	@wraps(test)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return test(*args, **kwargs)
		else:
			flash("necesitas loguearte primero")
			return redirect(url_for('users.login'))
	return wrap


################
#### routes ####
################

@app.route('/', defaults={'page':'index'})
def index(page):
	return redirect(url_for('tasks.tasks'))





