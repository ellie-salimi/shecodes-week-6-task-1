class Question:
    def __init__(self, question_text, answers):
        self.question_text = question_text
        self.answers = answers
    def get_answer_by_code(self):
       user_answer = input(self.question_text)
       return user_answer