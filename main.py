from Question import Question
from QuestionMaster import QuestionMaster
from question_list import questions

question_bank = [Question(question["question"],question["answer"])for question in questions]

question_master = QuestionMaster(question_bank)
question_master.start_quiz()