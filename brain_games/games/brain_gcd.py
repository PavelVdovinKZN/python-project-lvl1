#!/usr/bin/env python
import random
from brain_games.scripts.common_logic import welcome, name, run

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
    print("Question: " + str(num1) + ' ' + str(num2))
    run(correct_answer, name)
    if i == 2:
        print("Congratulations, " + name + "!")


def main():
    pass


if __name__ == '__main__':
    main()
