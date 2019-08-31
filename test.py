from Survey import Survey
from Question import Question
from Section import Section



my_survey = Survey('SheCodes')
my_survey.start_survey()
my_survey.ask_qualifying_questions()
my_survey.start_survey_sections()
my_survey.ask_question()
my_survey.end()