#!/usr/bin/env python
import random
import sys

from brain_games.cli import name
from brain_games.scripts.brain import welcome

welcome()
name = name()

print("What number is missing in the progression?")


def random_progression():
    for i in range(3):
        start_num = random.randint(1, 10)
        step = random.randint(1, 10)
        list1 = [start_num + step]
        for y in range(9):
            num = list1[-1]
            list1.append(num + step)
        random_num = random.randint(1, 9)                           # выбираем число из списка, которое спрячем
        correct_answer = list1.pop(random_num)                      # удаляем из списка это число
        list1.insert(random_num, "..")                              # ставим вместо него двоеточие
        print("Question: " + str(list1))
        user_answer = int(input("Your answer: "))                   # ответ пользователя
        if user_answer == correct_answer:
            print("Correct!")
            i += 1
        else:
            print("'" + str(user_answer) + "' is wrong answer ;(. Correct answer was "
                  + "'" + str(correct_answer) + "'" ".\nLet's try again, {0}!".format(name))
            sys.exit()


random_progression()

print("Congratulations, {0}!".format(name))


def main():
    pass


if __name__ == '__main__':
    main()
