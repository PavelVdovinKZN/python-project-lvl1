#!/usr/bin/env python
import random
import sys


from brain_games.scripts.brain import name_user, welcome_user

welcome = welcome_user()
name_us = name_user()

print("What is the result of the expression?")


def calc():
    for i in range(3):
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        ar_action = random.randint(1, 3)
        if ar_action == 1:
            operand = "+"
            correct_answer = num1 + num2
        elif ar_action == 2:
            operand = "-"
            correct_answer = num1 - num2
        else:
            operand = "*"
            correct_answer = num1 * num2
        print("Question: " + str(num1) + ' ' + operand + ' ' + str(num2))
        user_answer = int(input("Your answer: "))
        if user_answer == correct_answer:
            print("Correct!")
            i += 1
        else:
            print('\'{0}\' is wrong answer ;(. Correct answer was'
                  ' \'{1}{2}'.format(str(user_answer), str(correct_answer),
                                     "'" ".\nLet's try again, {0}!".format(
                                         name_us)))
            sys.exit()


calc()

print("Congratulations, {0}!".format(name_us))


def main():
    pass


if __name__ == '__main__':
    main()
