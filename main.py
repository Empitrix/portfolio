from flask import Flask
from flask import render_template
from flask import request
from src.database.database import Database


app = Flask(__name__)


@app.route('/', methods = ["POST", "GET"])
def index():
	Database()
	if request.method == "POST":
		print(request.method.index)
		print(request.form[""])

	return render_template('index.html');


@app.route('/projects')
def projects():
	return render_template('projects.html');


@app.route('/blog')
def blog():
	return render_template('blog.html');


if __name__ == "__main__":
	app.run(debug=True)

