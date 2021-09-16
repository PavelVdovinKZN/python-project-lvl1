#!/usr/bin/env python
from random import randint

TASK_DESCRIPTION = ('Answer "yes" if the number is even, '
                    'otherwise answer "no".')

FIRST_NUMBER = 1
SECOND_NUMBER = 10


def get_game_round():
    rand_num = randint(FIRST_NUMBER, SECOND_NUMBER)
    if rand_num % 2 == 0:
        correct_answer = "yes"
    else:
        correct_answer = "no"
    return str(rand_num), str(correct_answer)
