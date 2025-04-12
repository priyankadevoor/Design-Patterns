class Answer:
    def __init__(self, content, author):
        self.id = id(self)
        self.content = content
        self.author = author
        self.comments = []
    
    def get_answer(self):
        return self.content
    
    def get_author(self):
        return self.author
    
    def add_comment(self, comment):
        self.comments.append(comment)
    
    def get_comments(self):
        comments = ''
        for comment in self.comments:
            comments += comment.get_comment()
        return comments
    