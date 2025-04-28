from .utils import slugify

class Note:
    def __init__(self, title, body):
        self.title = title
        self.body = body

#how can i make use of slugify in here in snippet function
    def snippet(self):
        return slugify(self.body[:20])

    def __repr__(self):
        return f"<Note {self.title!r}>"