class Section:
    def __init__(self, section_name, section_desc,s_questions):
        self.section_name = section_name
        self.section_desc = section_desc
        self.s_questions = s_questions
        # self.user_section_answers=[]
        # print('**************************'+self.section_name+'*************************\n')
        # print('Description:  '+self.section_desc+ '\n\n')
        # for q in range(len(self.s_questions)):
        #     print(self.s_questions[q])
        #     user_answer_signle=input()
        #     self.user_section_answers.append(user_answer_signle)
        # print('\n\n These are your answers: '+ str(self.user_section_answers))