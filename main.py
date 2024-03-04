from flask import Flask
from flask import render_template
from flask import request
from src.models.blog_post import BlogPost
from src.database.database import Database

# from flask_gfm import Markdown
# from flask_misaka import Misaka
# from flaskext.markdown import Markdown


app = Flask(__name__)
# Misaka(app)
# Markdown(app)


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
	posts:list[BlogPost] = Database().load_posts()
	return render_template('blog.html', posts=posts);

@app.route('/blog/<id>')
def blog_post(id):
	posts:list[BlogPost] = Database().load_posts()
	for post in posts:
		if post.id == int(id, 16):
			return render_template('blog_post.html', post=post);
	return "BLOG POST NOT FOUND !"


@app.route('/admin')
def admin():
	return "<h1>ADMIN!</h1>";

# # {404 page}
# app.errorhandler(404)
# def page_not_found():
# 	# return render_template('404.html'), 404
# 	return "Awesome!", 404


if __name__ == "__main__":
	app.run(debug=True)

