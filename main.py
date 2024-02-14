from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/')
def index():
	return render_template('index.html');

@app.route('/projects')
def projects():
	return render_template('projects.html');

@app.route('/blog')
def blog():
	return render_template('blog.html');

if __name__ == "__main__":
	app.run(debug=True)

