from datetime import datetime, timedelta
# Current formating of date-time: %Y-%m-%d %H:%M:%S


class BlogPost:
	def __init__(
			self,
			id:int,
			title:str,
			content:str,
			visibility:bool,
			tags:str,
			last_edit:datetime) -> None:
		"""Blog Post"""
		self.id = id
		self.title = title
		self.tags = tags
		self.visibility = visibility
		self.content = content
		self.last_edit = last_edit
		# self.__date_format = '%Y-%m-%d %H:%M:%S'

	def to_json(self, database=False) -> dict[str, int | str | None]:
		"""Return as valid json"""
		return {
			"id": None if database == True else self.id,
			"title": self.title,
			"visibility": int(self.visibility) if database else self.visibility,
			"tags": self.tags,
			"content": self.content,
			"lastEdit":self.last_edit.strftime("%Y-%m-%d %H:%M:%S"),
		}
	
	def zero_last_edit(self) -> None:
		"""Updates last edit to current time (last time edited)"""
		self.last_edit = datetime.now()

	def get_time(self) -> str:
		"""Get LastEdit as the past time"""
		timing:timedelta = datetime.now() - self.last_edit
		# timing = datetime.now() - datetime.strptime("2020-11-21 20:45:5", "%Y-%m-%d %H:%M:%S");
		# print(timing)
		times:dict[str, int] = {
			"year": timing.days // 365,
			"month": timing.days // 30 % 12,
			"day": timing.days % 30,
			"hour": timing.seconds // 3600,
			"minute": timing.seconds // 60 % 60,
			"second": timing.seconds % 60} 
		for k, v in times.items():
			if v != 0:
				return f"{v} {k}{'s' if v > 1 else ''} ago"

		return ""


def parse_blog_post(inpt: dict[str, int | str | bool]) -> BlogPost:
	"""Parse valid json to BlogPost"""
	return BlogPost(
		id=inpt['id'] if type(inpt['id']) is int else 0,
		tags=inpt['tags'] if type(inpt['tags']) is str else "",
		visibility= bool(inpt['visibility']),
		title=inpt['title'] if type(inpt['title']) is str else "",
		content=inpt['content'] if type(inpt['content']) is str else "",
		last_edit=datetime.strptime(
			inpt['lastEdit'] if type(inpt['lastEdit']) is str else "",
			'%Y-%m-%d %H:%M:%S'),
	)

