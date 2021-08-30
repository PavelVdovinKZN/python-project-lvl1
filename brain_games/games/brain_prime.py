#!/usr/bin/env python
import random
from brain_games.scripts.common_logic import welcome, name, run

welcome()
name = name()

print('Answer "yes" if given number is prime. Otherwise answer "no".')

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
    run(correct_answer, name)
    if i == 2:
        print("Congratulations, " + name + "!")


def main():
    pass


if __name__ == '__main__':
    main()
