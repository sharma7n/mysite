from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
boots = Bootstrap(app)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about/")
def about():
    return "Implement me!"

@app.route("/projects/")
def projects():
    return "Implement me!"

@app.route("/contact/")
def contact():
    return "Implement me!"

if __name__ == '__main__':
    app.run(debug=True)
