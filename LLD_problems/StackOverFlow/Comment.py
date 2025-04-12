class Comment:
    def __init__(self, content, author) -> None:
        self.id = id(self)
        self.content = content
        self.author = author

    def get_comment(self):
        return self.content
    
    def get_author(self):
        return self.author