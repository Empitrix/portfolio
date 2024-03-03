from datetime import datetime
from src.models.blog_post import BlogPost
from src.database.database import Database

db:Database = Database();


post0:BlogPost = BlogPost(
	id=1,
	title="Item No.1",
	content="Content No.1",
	tags="Subtitle No.1",
	last_edit=datetime.now()
);

post1:BlogPost = BlogPost(
	id=0,
	title="Item No.2",
	content="Content No.2",
	tags="Subtitle No.2",
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
db.load_posts()[0].get_time()
print(db.load_posts()[0].get_time())

