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

    def post_question(self, title):
        question = Question(title, self)
        self.questions.append(question)
        return question

    def post_answer(self, question, content):
        answer = Answer(content, self)
        question.add_answer(answer)
        return answer

    def add_comment(self, ques_or_ans_obj, content):
        comment = Comment(content, self)
        ques_or_ans_obj.add_comment(comment)