from flask import Flask
from flask import render_template
from flask import request
from src.models.blog_post import BlogPost
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
	posts:list[BlogPost] = Database().load_posts()
	return render_template('blog.html', posts=posts);

@app.route('/blog/<id>')
def blog_post(id):
	# num_id = int(id, 16)
	# print(f"NUM ID: {num_id}")
	posts:list[BlogPost] = Database().load_posts()
	for post in posts:
		if post.id == int(id, 16):
			return render_template('blog_post.html', post=post);

	# post = [p for p in posts if p.id == id] 
	# if len(post) == 0:
	# 	return "BLOG POST NOT FOUND !"
	# return render_template('blog_post.html', post=post[0]);
	return "BLOG POST NOT FOUND !"


if __name__ == "__main__":
	app.run(debug=True)

