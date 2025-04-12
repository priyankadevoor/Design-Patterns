class Question:

    def __init__(self, title, author):
        self.id = id(self)
        self.title = title
        self.author = author
        self.answers = []
        self.comments = []
        self.votes = []

    def get_answers(self):
        answers = ''
        for answer in self.answers:
            answers += answer.get_answer() + '\n'
        return answers
    
    def add_answer(self, answer):
        self.answers.append(answer)

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