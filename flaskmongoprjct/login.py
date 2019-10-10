from flask import Flask, render_template, url_for, request, session, redirect
from flask_pymongo import PyMongo
import bcrypt


app= Flask(__name__)
app.config['SECRET_KEY'] = '822d20c4d8c1e68a9bc804543259d1f383ef099dc25f7035'


app.config['MONGO_DBNAME'] = 'school'
app.config['MONGO_URI'] = 'mongodb+srv://SheetalK01:SVKME2015@sheetalkcluster-xtvj5.mongodb.net/school?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/')
def index():
	if 'username' in session:
		return "Welcome to your workspace: " + session['username']
	return render_template('index.html')

@app.route('/login',methods=['POST'])
def login():
    students=mongo.db.students
    login_users=students.find_one({'emailid':request.form['username']})

    if login_users:
    	if bcrypt.hashpw(request.form['pass'].encode('utf-8'),login_users['password'].encode('utf-8')) ==login_users['password'].encode('utf-8'):
    		session['username']=request.form['username']
    		return redirect(url_for('index'))

	return 'invalid username/password combination'

	'''	students=mongo.db.students
	login_usr=students.find_one({'emailid':request.form['emailid']})

	if login_usr:
		if bcrypt.hashpw(request.form['pass'].encode('utf-8'), login_usr['password'].encode('utf-8')) == login_usr['password'].encode('utf-8'):
			session['uname'] = request.form['studname']
			return redirect(url_for('index'))


	return 'Invalid username/password combination'''
	

@app.route('/register',methods=['POST','GET'])
def register():
	if request.method == 'POST':
		students = mongo.db.students
		current_user=students.find_one({'name':request.form['username']})

		if current_user is None:
			hashpass=bcrypt.hashpw(request.form['pass'].encode('utf-8'),bcrypt.gensalt())
			students.insert({'name':request.form['name'],'password':hashpass,'rollno':request.form['rollno'],'emailid':request.form['username'],'standard':request.form['std']})
			session['username'] = request.form['username']
			return redirect(url_for('index'))

		return 'username already exists'

	return render_template('register.html')
	
if __name__ == '__main__':
	app.run(debug=True)


'''students = mongo.db.students
		existinguser=students.find_one({'name':request.form['studname']})


		if existinguser is None:
			hashpass=bcrypt.hashpw(request.form['pass'].encode('utf-8'),bcrypt.gensalt())
			students.insert({'name':request.form['studname'],'password':hashpass,'rollno':request.form['rollno'],'emailid':request.form['emailid'],'standard':request.form['standard']})
			session['uname'] = request.form['studname']
			return redirect(url_for('index'))
		return 'username already exists'
	
		return render_template('register.html')'''
