#!/usr/bin/env python
import random
import sys

from brain_games.cli import name
from brain_games.scripts.brain import welcome

welcome()
name = name()

print("Find the greatest common divisor of given numbers.")

for i in range(3):
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    correct_answer = num1 + num2
    print(str(num1) + ' ' + str(num2))
    user_answer = int(input("Your answer: "))
    if user_answer == correct_answer:
        print("Correct!")
        i += 1
    else:
        print("'" + str(user_answer) +
              "' is wrong answer ;(. Correct answer was "
              + "'" + str(correct_answer) +
              "'" ".\nLet's try again, {0}!".format(name))
        sys.exit()

print("Congratulations, {0}!".format(name))


def main():
    pass


if __name__ == '__main__':
    main()
