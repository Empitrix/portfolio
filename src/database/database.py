from typing import Union
from ..models.blog_post import BlogPost
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


	def new_post(self, post:BlogPost) -> None:
		"""New Blog Post"""
		self.cursor.execute("""""")
		self.conn.commit()

	def update_post(self, post:BlogPost) -> None:
		"""Update Given Post"""
		pass

	def delete_post(self, post:Union[BlogPost, int]) -> None:
		"""Delete Given Post by itself or it's id"""
		pass


	def load_posts(self) -> list[BlogPost]:
		"""Load all the posts"""
		return []
