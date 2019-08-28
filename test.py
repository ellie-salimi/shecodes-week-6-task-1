from Survey import Survey
from Question import Question
from Section import Section

qualifying_questions = [
    "Are you part of Shecodes program?\n(a) Yes! \n(b) No!\n(c)What's Shecodes?\n",
    "What do you think of being a programmer?\n(a) Hate it!\n(b) What's a programmer\n(c) That's awsome\n" ,
    "Which programming language you are learning now?\n(a) Java\n(b) C#\n(c) Python\n",
]
questions_section_1=[
    'Q1-1?\n a: Answer 1\n b: Answer 2\n c: Answer 3\n',
    'Q1-2?\n a: Answer 1\n b: Answer 2\n c: Answer 3\n',
    'Q1-3?\n a: Answer 1\n b: Answer 2\n c: Answer 3\n',
]
section_1 = Section('section1','This is section 1 and because of the quilifying question 1',questions_section_1)
# print(section_1.call_section())
questions_section_2=[
    'Q2-1?\n a: Answer 1\n b: Answer 2\n c: Answer 3\n',
    'Q2-2?\n a: Answer 1\n b: Answer 2\n c: Answer 3\n',
    'Q2-3?\n a: Answer 1\n b: Answer 2\n c: Answer 3\n',
]
section_2 = Section('section2','This is section 2 and because of the quilifying question 2',questions_section_2)
questions_section_3=[
    'Q3-1?\n a: Answer 1\n b: Answer 2\n c: Answer 3\n',
    'Q3-2?\n a: Answer 1\n b: Answer 2\n c: Answer 3\n',
    'Q3-3?\n a: Answer 1\n b: Answer 2\n c: Answer 3\n',
]
section_3 = Section('section3','This is section 3 and because of the quilifying question 3',questions_section_3)
my_sections = {
0: section_1,
1: section_2,
2: section_3
}


my_survey = Survey(my_sections,'SheCodes')
my_survey.start_survey()
my_survey.ask_qualifying_questions(qualifying_questions)
my_survey.start_survey_sections()