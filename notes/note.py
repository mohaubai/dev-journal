class Note:
    def __init__(self, title, body):
        self.title = title
        self.body = body

    def __repr__(self):
        return f"<Note {self.title!r}>"