from Question import Question
from Answer import Answer
from Comment import Comment

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.questions = []
        self.answers = []
        self.comments = []

    def post_question(self, title, author):
        question = Question(title, author)
        self.questions.append(question)
        return question

    def post_answer(self, question, content, author):
        answer = Answer(content, author)
        question.add_answer(answer)

    def add_comment(self, ques_or_ans_obj, content, author):
        comment = Comment(content, author)
        ques_or_ans_obj.add_comment(comment)