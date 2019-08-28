class Survey(object):
    def __init__(self, survey_sections,survey_name):
        self.survey_sections = survey_sections
        self.survey_name = survey_name
        self.user_q_answers=[]
        self.eligiable_section = 'You are not qualified'


    def start_survey(self):
       print('Welcome to ' + self.survey_name +' survey\n')
       print('This Survey is based on your experience in Shecodes Plus program\n')


    def ask_qualifying_questions(self, qualifying_questions):
        for q in range(len(qualifying_questions)):
            print(qualifying_questions[q])
            user_answer=input()
            self.user_q_answers.append(user_answer)
        print('\n\n These are your answers: '+ str(self.user_q_answers))
    def start_survey_sections(self):
        
        if self.user_q_answers[0] == 'a' :
            self.eligiable_section=self.survey_sections[0]
        elif self.user_q_answers[1] == 'c':
            self.eligiable_section=self.survey_sections[1]
        elif self.user_q_answers[2] == 'c':
            self.eligiable_section=self.survey_sections[2]
        else:
            print('Sorry you are not quilify for this survey!')
        return  self.eligiable_section


    # def ask_question(self):
    #     self.user_section_answers=[]
    #     print('**************************'+self.section_name+'*************************\n')
    #     print('Description:  '+self.section_desc+ '\n\n')
    #     for q in range(len(self.s_questions)):
    #         print(self.s_questions[q])
    #         user_answer_signle=input()
    #         self.user_section_answers.append(user_answer_signle)
    #     print('\n\n These are your answers: '+ str(self.user_section_answers))


    # def show_answers(self):
    # def answer_question(self):
    # def go_to_next_question(self):
    # def end(self):