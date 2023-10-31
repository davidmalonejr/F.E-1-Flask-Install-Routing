from markupsafe import escape
from flask import Flask, abort

app = Flask(__name__)


@app.route('/')
@app.route('/index/')
def genius():
	return '<h1>Welcome To David\'s Website!</h1>'


@app.route('/about/')
def about():
	return '<h3>Originally from Cleveland, Ohio, David Malone Jr. serves as the Senior Innovation Educator, Curriculum Lead at The Hidden Genius Project. Soon after receiving his B.S. in Computer Engineering from the University of Akron, he moved to Oakland in order to pursue his passion of uplifting Black communities. The under-representation of Black people in the tech industry sparked an interest for David to help provide the resources and opportunities needed to diversify the tech sector. He also worked as a Technical Support Representative for Rockwell Automation overseeing numerous software products.!</h3>'


@app.route('/rep_yo_city/<city>/<state>')
def capitalize(city,state):
	return '<h1>{}</h1>'.format(escape(city.capitalize()+", "+state.capitalize()))


# Calculator Functionality
@app.route('/add/<int:n1>/<int:n2>/')
def add(n1,n2):
	return '<h1>{}</h1>'.format(n1+n2)

@app.route('/sub/<int:n1>/<int:n2>/')
def sub(n1,n2):
	return '<h1>{}</h1>'.format(n1-n2)

@app.route('/mult/<int:n1>/<int:n2>/')
def mult(n1,n2):
	return '<h1>{}</h1>'.format(n1*n2)

@app.route('/div/<int:n1>/<int:n2>/')
def div(n1,n2):
	return '<h1>{}</h1>'.format(n1/n2)


@app.route('/mod/<int:n1>/<int:n2>/')
def mod(n1,n2):
	return '<h1>{}</h1>'.format(n1%n2)



@app.route('/geniuses/<int:user_id>/')
def greet_user(user_id):
	users = ['Alvin', 'Boyd', 'Craig','Damonie','Derek','Edward','Enansi','Isaiah I.', 'Isaiah M.', 'Jaden','Jordan','Matthew','Moriah','Noah','Prinzton','Tahir','Talib','Tyler', 'Wendell', 'Zion']
	try:
		return '<h2> Hi {}</h2>'.format(users[user_id])
	
	except IndexError:
		abort(404)
