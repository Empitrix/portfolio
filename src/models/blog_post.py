from datetime import datetime
# Current formating of date-time: %Y-%m-%d %H:%M:%S


class BlogPost:
	def __init__(
			self,
			id:int,
			title:str,
			content:str,
			tags:str,
			last_edit:datetime) -> None:
		"""Blog Post"""
		self.id = id
		self.title = title
		self.tags = tags
		self.content = content
		self.last_edit = last_edit
		self.__date_format = '%Y-%m-%d %H:%M:%S'

	def to_json(self, database=False) -> dict[str, int | str | None]:
		"""Return as valid json"""
		return {
			"id": None if database == True else self.id,
			"title": self.title,
			"tags": self.tags,
			"content": self.content,
			"lastEdit":self.last_edit.strftime(self.__date_format),
		}
	
	def zero_last_edit(self) -> None:
		"""Updates last edit to current time (last time edited)"""
		self.last_edit = datetime.now()


def parse_blog_post(inpt: dict[str, int | str]) -> BlogPost:
	"""Parse valid json to BlogPost"""
	return BlogPost(
		id=inpt['id'] if type(inpt['id']) is int else 0,
		tags=inpt['tags'] if type(inpt['tags']) is str else "",
		title=inpt['title'] if type(inpt['title']) is str else "",
		content=inpt['content'] if type(inpt['content']) is str else "",
		last_edit=datetime.strptime(
			inpt['lastEdit'] if type(inpt['lastEdit']) is str else "",
			'%Y-%m-%d %H:%M:%S'),
	)

