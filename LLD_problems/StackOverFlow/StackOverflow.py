"""
Entities -
1. User
    - name
    - email_id
    - ask_question()
    - answer_question()
    - add_comment()
    - vote

2. Question
    - id
    - title
    - author
    - tags
    - votes
    - comments
    - answers

3. Answer
    - id
    - content
    - author
    - votes
    - comments
4. Comment
    - id
    - content
    - author
5. Vote
    - user
    - value
6. Tag
    - id
    - name
7. Stack_Overflow
    - users
    - create_user()
    - post_question()
    - answer_question()
    - vote()
    - get_question(tag)
"""
from User import User

class Stack_Overflow:
    def __init__(self):
        self.questions = []
        self.answers = []
        self.users = []

    def create_user(self, name, email):
        user = User(name, email)
        self.users.append(user)

    def post_question(self, title, author):
        question = Question(title, author)
        self.questions.append(question)
        return question

    def post_answer(self, question, content, author):
        answer = Answer(content, author)
        question.add_answer(answer)
    
    def get_answers(self, question):
        return question.get_answers()
    
    def add_comment(self, ques_or_ans_obj):

    

stack_overflow = Stack_Overflow()
priya = stack_overflow.create_user('Priyanka', 'priyadevoor@gmail.com')
shiv = stack_overflow.create_user('Shivani', 'shivanidevoor@gmail.com')
ques1 = stack_overflow.post_question('How much is 2+2', priya)
stack_overflow.post_answer(ques1, 'Answer is 4', shiv)
answer1 = stack_overflow.get_answers(ques1)
print(answer1)
