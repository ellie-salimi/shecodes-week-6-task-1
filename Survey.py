from Section import Section
from Question import Question


class Survey:
    def __init__(self,survey_name):
        self.survey_sections = {}
        self.survey_name = survey_name
        self.user_q_answers=[]
        self.eligiable_section = 'You are not qualified'
        self.questions_section_1=[
        'Q1-1?\n a: Answer 1\n b: Answer 2\n c: Answer 3\n',
        'Q1-2?\n a: Answer 1\n b: Answer 2\n c: Answer 3\n',
        'Q1-3?\n a: Answer 1\n b: Answer 2\n c: Answer 3\n',
         ]
        self.section_1 = Section('section1','This is section 1 and because of the quilifying question 1',self.questions_section_1)
        self.questions_section_2=[
        'Q2-1?\n a: Answer 1\n b: Answer 2\n c: Answer 3\n',
        'Q2-2?\n a: Answer 1\n b: Answer 2\n c: Answer 3\n',
        'Q2-3?\n a: Answer 1\n b: Answer 2\n c: Answer 3\n',
        ]
        self.section_2 = Section('section2','This is section 2 and because of the quilifying question 2',self.questions_section_2)
        self.questions_section_3=[
        'Q3-1?\n a: Answer 1\n b: Answer 2\n c: Answer 3\n',
        'Q3-2?\n a: Answer 1\n b: Answer 2\n c: Answer 3\n',
        'Q3-3?\n a: Answer 1\n b: Answer 2\n c: Answer 3\n',
        ]
        self.section_3 = Section('section3','This is section 3 and because of the quilifying question 3',self.questions_section_3)
        self.survey_sections = {
        0: self.section_1,
        1: self.section_2,
        2: self.section_3
    }


    def start_survey(self):
       print('Welcome to ' + self.survey_name +' survey\n')
       print('This Survey is based on your experience in Shecodes Plus program\n')

    
    def ask_qualifying_questions(self):
        self.qualifying_questions = [
        "Are you part of Shecodes program?\n(a) Yes! \n(b) No!\n(c)What's Shecodes?\n",
        "What do you think of being a programmer?\n(a) Hate it!\n(b) What's a programmer\n(c) That's awsome\n" ,
        "Which programming language you are learning now?\n(a) Java\n(b) C#\n(c) Python\n",
        ]
        for q in range(len(self.qualifying_questions)):
            print(self.qualifying_questions[q])
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


    def ask_question(self):
        self.user_section_answers=[]
        print('**************************'+self.eligiable_section.section_name+'*************************\n')
        print('Description:  '+self.eligiable_section.section_desc+ '\n\n')
        for q in range(len(self.eligiable_section.s_questions)):
            print(self.eligiable_section.s_questions[q])
            user_answer_signle=input()
            self.user_section_answers.append(user_answer_signle)
        print('\n\n These are your answers: '+ str(self.user_section_answers))

    # def show_answers(self):
    # def answer_question(self):
    # def go_to_next_question(self):
    def end(self):
        print('Thanks for participating!')