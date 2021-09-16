#!/usr/bin/env python
from random import randint

TASK_DESCRIPTION = "What number is missing in the progression?"
MIN_NUMBER = 1
MAX_NUMBER = 100
MIN_DIFF_PROGRESSION = 1
MAX_DIFF_PROGRESSION = 10
MIN_HIDDEN_NUMBER = 1
MAX_HIDDEN_NUMBER = 9


def build_progression(first_element, step):
    member, progression = first_element, [first_element]
    for i in range(9):
        member += step
        progression.append(member)
    return progression


def get_string_from_progression(progression, hidden_number):
    progression_string = []
    for index in range(0, 9):
        progression_string.append(str(progression[index]))
    progression_string[hidden_number] = '..'
    return " ".join(progression_string)


def get_game_round():
    first_element = randint(MIN_NUMBER, MAX_NUMBER)
    step = randint(MIN_DIFF_PROGRESSION, MAX_DIFF_PROGRESSION)
    hidden_number = randint(MIN_HIDDEN_NUMBER, MAX_HIDDEN_NUMBER)
    progression = build_progression(first_element, step)
    return (get_string_from_progression(progression, hidden_number),
            str(progression[hidden_number]))
