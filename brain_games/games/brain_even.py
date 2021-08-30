#!/usr/bin/env python
import random
from brain_games.scripts.common_logic import welcome, name, run

welcome()
name = name()

print("Answer \"yes\" if the number is even, otherwise answer \"no\".")

for i in range(3):
    rand_num = random.randint(0, 100)
    print("Question: " + str(rand_num))
    if rand_num % 2 == 0:
        correct_answer = "yes"
    else:
        correct_answer = "no"
    run(correct_answer, name)
    if i == 2:
        print("Congratulations, " + name + "!")


def main():
    pass


if __name__ == '__main__':
    main()
