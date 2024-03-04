from datetime import datetime
from src.models.blog_post import BlogPost
from src.database.database import Database

db:Database = Database();


post0:BlogPost = BlogPost(
	id=0,
	title="Ekko's README",
	visibility=True,
	content="""Ain't Non To it""",
	tags="Ekko | Corss-Platform | Application",
	last_edit=datetime.now()
);

post1:BlogPost = BlogPost(
	id=0,
	title="Testing MARKDOWN",
	content="""Nothing""",
	visibility=True,
	tags="Test | Markdown | Javascript",
	last_edit=datetime.now()
);



# # {SQL Injection Test}
# post2:BlogPost = BlogPost(
# 	id=0,
# 	title='''"""Some,'''"""'''A,""""Coul,, do'",
# 	content="Content No.2",
# 	tags="Subtitle No.2",
# 	last_edit=datetime.now()
# );
# # db.new_post(post2)
# # print(db.load_posts()[-1].title)




# db.new_post(post0);
# db.new_post(post1);

# db.load_posts();
#update_post posts:list[BlogPost] = db.load_posts();

# print(db.load_posts()[0].title)
# db.update_post(post0);
# print(db.load_posts()[1].last_edit)
# print(posts[0].last_edit)



# print(db.load_posts()[0].title)
# db.delete_post(db.load_posts()[0])
# # db.delete_post()
# print(db.load_posts()[0].title)

# db.new_post(post0)
print(db.load_posts())
# db.delete_post(db.load_posts()[0])
# print(db.load_posts())

# db.new_post(post0)

# p = db.load_posts()[0]
# print(p.title)
# print(p.visibility)
# p.visibility = not p.visibility
# print(p.visibility)
# db.update_post(p)

# for p in db.load_posts():
# 	db.delete_post(p)
# print(db.load_posts()[0].get_time())

