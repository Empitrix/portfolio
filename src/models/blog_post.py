from datetime import datetime
# Current formating of date-time: %Y-%m-%d %H:%M:%S


class BlogPost:
	def __init__(
			self,
			id:int,
			title:str,
			content:str,
			last_edit:datetime) -> None:
		"""Blog Post"""
		self.id = id
		self.title = title
		self.content = content
		self.last_edit = last_edit
		self.__date_format = '%Y-%m-%d %H:%M:%S'

	def to_json(self) -> dict[str, int | str]:
		"""Return as valid json"""
		return {
			"id": self.id,
			"title": self.title,
			"content": self.content,
			"last_edit":self.last_edit.strftime(self.__date_format),
		}


def parse_blog_post(inpt: dict[str, int | str]) -> BlogPost:
	"""Parse valid json to BlogPost"""
	return BlogPost(
		id=inpt['id'] if type(inpt['id']) is int else 0,
		title=inpt['title'] if type(inpt['title']) is str else "",
		content=inpt['content'] if type(inpt['content']) is str else "",
		last_edit=datetime.strptime(
			inpt['last_edit'] if type(inpt['last_edit']) is str else "",
			'%Y-%m-%d %H:%M:%S'),
	)

