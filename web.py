from flask import Flask,render_template, redirect, session, url_for, request
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from flask_sqlalchemy import SQLAlchemy
import os


app =Flask(__name__)
app.config['SECRET_KEY']='DRYTGVNBRVI'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'kunal.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

##################################################
################### FORM #########################

class InfoForm(FlaskForm):
	fname=StringField('Enter first name')
	password = StringField('Enter your password')
	submit=SubmitField('submit')


#################################################
################## DB TABLE #####################

class Account(db.Model):

	__tablename__ = 'users'

	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.Text)
	password = db.Column(db.Text)

	def __init__(self, username, password):
		self.username = username
		self.password = password

	
	def __repr__(self):
		lst = []
		lst.append(str(self.id))
		lst.append(self.username)
		lst.append(self.password)
		return '\n'.join(lst)


@app.route('/')
def index():
	data = Account.query.all()
	return render_template('index.html', data=data)

@app.route('/insert', methods=['GET','POST'])
def insert():
	form=InfoForm()
	if form.validate_on_submit():
		fname=form.fname.data
		password=form.password.data
		acc = Account(fname, password)
		db.session.add(acc)
		db.session.commit()
		return redirect(url_for('inserted'))
	return render_template('insert.html',form=form)


@app.route('/inserted')
def inserted():
	return redirect(url_for('index'))

@app.route('/delete')
def delete():
	id = request.args.get('id')
	todel = Account.query.get(id)
	db.session.delete(todel)
	db.session.commit()
	return redirect(url_for('index'))

if __name__ == '__main__':
	app.run(debug=True)