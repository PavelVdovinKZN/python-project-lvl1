#!/usr/bin/env python
import random
import sys

from brain_games.cli import name
from brain_games.scripts.brain import welcome

welcome()
name = name()
#  ans_question - совмещение вопроса с результатом математической операции

print("What is the result of the expression?")


for i in range(3):
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    ar_action = random.randint(1, 3)
    if ar_action == 1:
        operand = "+"
        ans_question = num1 + num2
    elif ar_action == 2:
        operand = "-"
        ans_question = num1 - num2
    else:
        ar_action = 3
        operand = "/"
        ans_question = num1 // num2

    print(str(num1) + ' ' + str(operand) + ' ' + str(num2))
    user_answer = int(input("Your answer: "))
    if user_answer == ans_question:
        print("Correct!")
        i += 1
    else:
        print("'" + str(user_answer) +
              "' is wrong answer ;(.Correct answer was "
              + "'" + str(ans_question) +
              "'" ".\nLet's try again, {0}!".format(name))
        sys.exit()

print("Congratulations, {0}!".format(name))


def main():
    pass


if __name__ == '__main__':
    main()
