"""
Extend to add tag feature. Can search questions based on tags.
"""
from User import User
from Vote import Vote

class Stack_Overflow:
    def __init__(self):
        self.questions = []
        self.answers = []
        self.users = []

    def create_user(self, name, email):
        user = User(name, email)
        self.users.append(user)
        return user

    def post_question(self, title, author):
        question = author.post_question(title)
        return question

    def post_answer(self, question, content, author):
        answer = author.post_answer(question, content)
        return answer

    def get_answers(self, question):
        return question.get_answers()
    
    def add_comment(self, ques_or_ans_obj, user, content):
        user.add_comment(ques_or_ans_obj, content)

    def vote_question(self, question, vote_value):
        vote = Vote(vote_value)
        question.add_vote(vote)

    def vote_answer(self, answer, vote_value):
        vote = Vote(vote_value)
        answer.add_vote(vote)

    def get_votes(self, ques_or_ans_obj):
        return ques_or_ans_obj.get_votes()
    

stack_overflow = Stack_Overflow()
priya = stack_overflow.create_user('Priyanka', 'priyadevoor@gmail.com')
shiv = stack_overflow.create_user('Shivani', 'shivanidevoor@gmail.com')
ques1 = stack_overflow.post_question('How much is 2+2', priya)
ans1 = stack_overflow.post_answer(ques1, 'Answer is 4', shiv)
stack_overflow.add_comment(ans1, priya, 'Thanks for the answer!')
answer1 = stack_overflow.get_answers(ques1)
comment1 = ans1.get_comments()
vote = stack_overflow.vote_answer(ans1, 5)
votes = stack_overflow.get_votes(ans1)
print(answer1 + '\n' + comment1, votes)
