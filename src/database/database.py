from ..models.blog_post import BlogPost, parse_blog_post
import sqlite3


class Database:
	def __init__(self) -> None:
		"""Website's Database OBJ"""
		self.conn = sqlite3.connect("database.db");
		self.cursor = self.conn.cursor()
		# Initialize
		blog_table = """CREATE TABLE IF NOT EXISTS posts (
			id INTEGER PRIMARY KEY,
			title TEXT,
			content TEXT,
			tags TEXT,
			lastEdit TEXT
		);"""
		self.cursor.execute(blog_table)
		self.conn.commit()  # Save changes


	def new_post(self, post:BlogPost) -> None:
		"""New blog post"""
		post_data = post.to_json(database=True);  # To create unique ID
		self.cursor.execute("""
			  INSERT INTO posts VALUES
			  (:id, :title, :content, :tags, :lastEdit)
		""", post_data)
		self.conn.commit()


	def update_post(self, post:BlogPost, update_time=True) -> None:
		"""Update Given Post by it's ID"""
		if update_time:
			post.zero_last_edit()  # Set last edit to now
		post_data = post.to_json()
		self.cursor.execute("""
			UPDATE posts SET
				title=:title,
				content=:content,
				tags=:tags,
				lastEdit=:lastEdit
			WHERE id=:id
		""", post_data)
		self.conn.commit()


	def delete_post(self, post:BlogPost) -> None:
		"""Delete Given Post by extracting it's ID"""
		# Create json data out of it
		parameter:dict[str, int] = {"id" : post.id}
		# Remove from db
		self.cursor.execute("""
			DELETE FROM posts WHERE id=:id
		""", parameter)
		self.conn.commit()  # Save changes


	def load_posts(self) -> list[BlogPost]:
		"""Load all the blog posts"""
		posts:list[BlogPost] = []
		for post in self.cursor.execute("SELECT * FROM posts"):
			json_data = {
				"id":post[0],
				"title":post[1],
				"content":post[2],
				"tags":post[3],
				"lastEdit":post[4]}
			current:BlogPost = parse_blog_post(json_data)
			posts.append(current)
		return posts

