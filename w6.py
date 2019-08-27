from Survey import Survey
from Question import Question
from Section import Section
# from Answer import Answer
my_sections =  {
            1 : 'Qualifying Questions',
            2 : 'Part 1',
            3 : 'Part 2',
            4 : 'Part 3'
        }

quilifying_questions = [
    "Are you part of Shecodes program?\n(a) Yes! \n(b) No!\n(c)What's Shecodes?\n\n",
    "What do you think of being a programmer?\n(a) Hate it!\n(b) What's a programmer\n(c) That's awsome\n\n" ,
    "Which programming language you are learning now?\n(a) Java\n(b) C#\n(c) Python\n\n",
]
questions = [
     Question(quilifying_questions[0], 'a'),
     Question(quilifying_questions[1], 'c'),
     Question(quilifying_questions[2], 'c')
]
for q in questions:
    if 


def get_answer(questions):
    score = 0
    for question in questions:
         user_answer = input(question.question_text)
         if user_answer == question.answer:
            score += 1
    print(score)
    if score == 0:
        print('Sorry you are not quilify for this survey!')
my_survey = Survey(my_sections,'SheCodes')
my_survey.start_survey()
get_answer(questions)



