#!/usr/bin/env python
from random import randint

TASK_DESCRIPTION = "What number is missing in the progression?"
START_PROGRESSION = 1
FINISH_PROGRESSION = 100
START_STEP_PROGRESSION = 1
FINISH_STEP_PROGRESSION = 10
START_HIDDEN_NUMBER = 1
FINISH_HIDDEN_NUMBER = 9


def game_round():
    progression = randint(START_PROGRESSION, FINISH_PROGRESSION)
    step_progression = randint(START_STEP_PROGRESSION, FINISH_STEP_PROGRESSION)
    hidden_number = randint(START_HIDDEN_NUMBER, FINISH_HIDDEN_NUMBER)
    list1 = [progression + step_progression]
    for y in range(9):
        num = list1[-1]
        list1.append(num + step_progression)
    correct_answer = list1[hidden_number]
    list1[hidden_number] = '..'
    question = ' '.join([str(num) for num in list1])
    return question, str(correct_answer)
