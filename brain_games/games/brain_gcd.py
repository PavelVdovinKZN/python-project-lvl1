#!/usr/bin/env python
from random import randint

TASK_DESCRIPTION = "Find the greatest common divisor of given numbers."

FIRST_NUMBER = 1
SECOND_NUMBER = 10


def get_game_round():
    num1 = randint(FIRST_NUMBER, SECOND_NUMBER)
    num2 = randint(FIRST_NUMBER, SECOND_NUMBER)
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    correct_answer = num1 + num2
    question = str(num1) + ' ' + str(num2)
    return str(question), str(correct_answer)
