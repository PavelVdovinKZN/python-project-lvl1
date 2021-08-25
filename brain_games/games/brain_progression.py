#!/usr/bin/env python
import random
import sys

from brain_games.scripts.brain import name_user, welcome_user

welcome = welcome_user()
name_us = name_user()

print("What number is missing in the progression?")


def random_progression():
    for i in range(3):
        start_num = random.randint(1, 10)
        step = random.randint(1, 10)
        list1 = [start_num + step]
        for y in range(9):
            num = list1[-1]
            list1.append(num + step)
        random_num = random.randint(1, 9)     # выбор числа, которое спрячем
        correct_answer = list1[random_num]    # берем число с индексом rand_num
        list1[random_num] = '..'              # ставим вместо него двоеточие
        print("Question: ", ', '.join([str(num) for num in list1]))
        user_answer = int(input("Your answer: "))
        if user_answer == correct_answer:
            print("Correct!")
            i += 1
        else:
            print(
                "\'{0}\' is wrong answer ;(.Correct answer was \'{1}{2}".format(
                    str(user_answer), str(correct_answer),
                    "'" ".\nLet's try again, {0}!".format(name_us)))
            sys.exit()


random_progression()

print("Congratulations, {0}!".format(name_us))


def main():
    pass


if __name__ == '__main__':
    main()
