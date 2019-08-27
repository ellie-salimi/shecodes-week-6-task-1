from Survey import Survey
from Question import Question
from Section import Section


my_sections =  {
            1 : 'Part 1',
            2 : 'Part 2',
            3 : 'Part 3',
        }

qualifying_questions = [
    "Are you part of Shecodes program?\n(a) Yes! \n(b) No!\n(c)What's Shecodes?\n",
    "What do you think of being a programmer?\n(a) Hate it!\n(b) What's a programmer\n(c) That's awsome\n" ,
    "Which programming language you are learning now?\n(a) Java\n(b) C#\n(c) Python\n",
]
my_survey = Survey(my_sections,'SheCodes')
my_survey.start_survey()
my_survey.ask_qualifying_questions(qualifying_questions)