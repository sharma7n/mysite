import datetime

from flask import Flask, render_template


app = Flask(__name__)

def years_since(start_date):
	delta = datetime.datetime.today() - start_date
	return int((delta.days + delta.seconds / 86400) / 365.2425)

@app.route("/")
def index():
	age = years_since(datetime.datetime(1988, 12, 4))
	experience = years_since(datetime.datetime(2013, 8, 7))
	return render_template('index.html', age=age, experience=experience)

@app.route("/games/")
def games():
	return render_template('games.html')

@app.route("/about/")
def about():
	pass

@app.route("/projects/")
def projects():
	pass

@app.route("/contact/")
def contact():
	pass

if __name__ == '__main__':
	app.run()
