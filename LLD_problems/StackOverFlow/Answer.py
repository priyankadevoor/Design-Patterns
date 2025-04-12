class Answer:
    def __init__(self, content, author):
        self.id = id(self)
        self.content = content
        self.author = author
        self.comments = []
        self.votes = []
    
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

    def add_vote(self, vote):
        self.votes.append(vote)
    
    def get_votes(self):
        val = 0
        for vote in self.votes:
            val += vote.get_value()
        return val