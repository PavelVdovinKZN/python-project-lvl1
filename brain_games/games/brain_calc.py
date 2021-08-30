#!/usr/bin/env python
import random
from brain_games.scripts.common_logic import welcome, name, run

welcome()
name = name()

print("What is the result of the expression?")

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
    run(correct_answer, name)
    if i == 2:
        print("Congratulations, " + name + "!")


def main():
    pass


if __name__ == '__main__':
    main()
