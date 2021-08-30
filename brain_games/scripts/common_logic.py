#!/usr/bin/env python
import sys


def welcome():
    print("Welcome to the Brain Games!")


def name():
    name_user = input(str('May I have your name? '))
    print('Hello, ' + name_user + "!")
    return name_user


def run(correct_answer, name_user):
    if type(correct_answer) == int:
        user_answer = int(input("Your answer: "))
    else:
        user_answer = str(input("Your answer: "))
    if user_answer == correct_answer:
        print("Correct!")
    else:
        print("'" + str(user_answer) +
              "' is wrong answer ;(. Correct answer was " + "'" +
              str(correct_answer) + "'.\nLet's try again, " + name_user + '!')
        sys.exit()


if __name__ == "__main__":
    pass
