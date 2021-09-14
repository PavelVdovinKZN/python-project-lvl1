#!/usr/bin/env python
from random import randint

TASK_DESCRIPTION = 'Answer "yes" if given number is prime. ' \
                   'Otherwise answer "no".'
FIRST_PRIME_NUM = 2
FIRST_NUMBER = 1
SECOND_NUMBER = 100


def check_of_prime(rand_num):
    if rand_num < FIRST_PRIME_NUM:
        return False
    for i in range(FIRST_PRIME_NUM, rand_num // 2 + 1):
        if rand_num % i == 0:
            return False
    return True


def game_round():
    rand_num = randint(FIRST_NUMBER, SECOND_NUMBER)
    correct_answer = 'yes' if check_of_prime(rand_num) else 'no'
    return str(rand_num), str(correct_answer)
