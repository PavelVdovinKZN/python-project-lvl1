#!/usr/bin/env python
import random
import sys

from brain_games.cli import name
from brain_games.scripts.brain import welcome

welcome()
name = name()

print('Answer "yes" if given number is prime. Otherwise answer "no".')


def prime():
    for i in range(3):
        rand_num = random.randint(2, 20)
        print('Question: ' + str(rand_num))
        k = 0
        for y in range(2, rand_num // 2 + 1):
            if rand_num % y == 0:
                k = k + 1
        if k <= 0:
            correct_answer = "yes"
        else:
            correct_answer = "no"
        user_answer = input("Your answer: ")
        if user_answer == correct_answer:
            print("Correct!")
            i += 1
        else:
            print("'" + str(user_answer) +
                  "' is wrong answer ;(. Correct answer was "
                  + "'" + str(correct_answer) +
                  "'" ".\nLet's try again, {0}!".format(name))
            sys.exit()


prime()

print("Congratulations, {0}!".format(name))


def main():
    pass


if __name__ == '__main__':
    main()
