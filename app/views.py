# views.py

from flask import Flask, flash, redirect, render_template, request, session, url_for
from functools import wraps
from flask.ext.sqlalchemy import SQLAlchemy
from forms import AddTaskForm, RegisterForm, LoginForm


app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

# Importamos el Modelo
from models import Task, User


####### Registro de usuario ######
@app.route('/register/', methods=['GET', 'POST'])
def register():
	error = None
	form = RegisterForm(request.form)
	if request.method == 'POST':
		if form.validate_on_submit():
			new_user = User(
				form.name.data,
				form.email.data,
				form.password.data,
			)
			db.session.add(new_user)
			db.session.commit()
			flash("Gracias por registrate, Por favor Accesa")
			return redirect(url_for('login'))
		else:
			return render_template('register.html', form=form, error=error)
	if request.method == 'GET':
		return render_template('register.html', form=form)



def login_required(test):
	@wraps(test)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return test(*args, **kwargs)
		else:
			flash("necesitas loguearte primero")
			return redirect(url_for('login'))
	return wrap



@app.route('/logout/')
def logout():
	session.pop('logged_in', None)
	session.pop('user_id', None)
	flash("Haz cerrado tu session. Bye!")
	return redirect(url_for('login'))


######### Login ##########
@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    form = LoginForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            u = User.query.filter_by(
                name=request.form['name'],
                password=request.form['password']
            ).first()
            if u is None:
                error = 'Opss Usuario Incorrecto'
                return render_template(
                    "login.html",
                    form=form,
                    error=error
                )
            else:
                session['logged_in'] = True
                session['user_id'] = u.id
                flash('Bingo! Estas adentro!!')
                return redirect(url_for('tasks'))
        else:
            return render_template(
                "login.html",
                form=form,
                error=error
            )
    if request.method == 'GET':
        return render_template('login.html', form=form)



@app.route('/tasks/')
@login_required
def tasks():
	open_tasks = db.session.query(Task).filter_by(status='1').order_by(Task.due_date.asc())
	closed_tasks = db.session.query(Task).filter_by(status='0').order_by(Task.due_date.asc())
	return render_template('tasks.html', form=AddTaskForm(request.form), open_tasks=open_tasks, closed_tasks=closed_tasks)


######### Nueva Tarea########
@app.route('/add/', methods=['GET','POST'])
@login_required
def new_task():
	import datetime
	error = None
	form = AddTaskForm(request.form)
	if request.method == 'POST':
		if form.validate_on_submit():
			new_task = Task(form.name.data, form.due_date.data, form.priority.data, datetime.datetime.utcnow(), '1', session['user_id'])
			db.session.add(new_task)
			db.session.commit()
			flash("Nuevo registro agregado con Exito! relax..")
			return redirect(url_for('tasks'))
		else:
			return render_template('tasks.html', form=form, error=error)
	if request.method == 'GET':
		return render_template('tasks.html', form=form)


#Marcar Tarea como completa
@app.route('/complete/<int:task_id>/')
@login_required
def complete(task_id):
	new_id = task_id
	db.session.query(Task).filter_by(task_id=new_id).update({"status": "0"})
	db.session.commit()
	flash('Tares Completada, relajate!!')
	return redirect(url_for('tasks'))


#Borrar una Tarea
@app.route('/delete/<int:task_id>/')
@login_required
def delete_entry(task_id):
	new_id = task_id
	db.session.query(Task).filter_by(task_id=new_id).delete()
	db.session.commit()
	flash('Tarea borrada !! Nice, echate Otra!')
	return redirect(url_for('tasks'))




