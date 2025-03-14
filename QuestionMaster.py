from multiprocessing.connection import answer_challenge
from images import win_image,lose_image,starting_image
from Question import Question
from typing import List
import random

class QuestionMaster:
    def __init__(self, q_list: List[Question]):
        self.q_list = q_list
        self.q_number = 1
        self.score = 0

    def start_quiz(self):
        print(starting_image)
        while self.q_number<=10:
            self.display_next_question()
        print(f"Quiz is over,you scored {self.score}")
        if self.score==10:
            print(win_image)
        else:
            print(lose_image)

    def display_next_question(self):
        next_question = self.q_list[random.randint(0,len(self.q_list))-1]
        print(f'Question {self.q_number}: {next_question.question}')
        answer=input("True or False: ")

        while answer !="True" and answer!="False":
            print()
            answer=input("True or False: ")

        if bool(answer) == next_question.answer:
            print("correct")
            self.score+=1
        else:
            print("you are wrong 🤪")
        
        self.q_number += 1
        print()

    
