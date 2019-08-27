class Survey():
    def __init__(self, survey_sections,survey_name):
        self.survey_sections = survey_sections
        self.survey_name = survey_name
        self.user_q_answers=[]


    def start_survey(self):
       print('Welcome to ' + self.survey_name +' survey\n')
       print('This Survey is based on your experience in Shecodes Plus program\n')


    def ask_qualifying_questions(self, qualifying_questions):
        for q in range(len(qualifying_questions)):
            print(qualifying_questions[q])
            user_answer=input()
            self.user_q_answers.append(user_answer)
        print(self.user_q_answers)
    def start_survey_sections(self):
        if self.user_q_answers[0] == 'a' :
            print(self.survey_sections[1])
        elif self.user_q_answers[1] == 'c':
            print(self.survey_sections[2])
        elif self.user_q_answers[2] == 'c':
            print(self.survey_sections[3])
        else:
            print('Sorry you are not quilify for this survey!')


    # def ask_question(self):
    # def show_answers(self):
    # def answer_question(self):
    # def go_to_next_question(self):
    # def end(self):