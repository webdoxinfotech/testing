from flask import Flask,render_template, redirect, session, url_for
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField

app =Flask(__name__)
app.config['SECRET_KEY']='DRYTGVNBRVI'

class InfoForm(FlaskForm):
	fname=StringField('Enter first name')
	password = StringField('Enter your password')
	submit=SubmitField('submit')


@app.route('/', methods=['GET','POST'])
def index():
	form=InfoForm()
	if form.validate_on_submit():
		session['fname']=form.fname.data
		session['password']=form.password.data
		return redirect(url_for('thankyou'))
	return render_template('index.html',form=form)

@app.route('/thankyou')
def thankyou():
	return render_template('thankyou.html')

if __name__ == '__main__':
	app.run(debug=True)