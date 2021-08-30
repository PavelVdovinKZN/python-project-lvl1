#!/usr/bin/env python
import random
from brain_games.scripts.common_logic import welcome, name, run

welcome()
name = name()

print("What number is missing in the progression?")

for i in range(3):
    start_num = random.randint(1, 10)
    step = random.randint(1, 10)
    list1 = [start_num + step]
    for y in range(9):
        num = list1[-1]
        list1.append(num + step)
    random_num = random.randint(1, 9)          # выбор числа, которое спрячем
    correct_answer = list1[random_num]         # берем число с индексом rand_num
    list1[random_num] = '..'                   # ставим вместо него двоеточие
    print("Question:", ' '.join([str(num) for num in list1]))
    run(correct_answer, name)
    if i == 2:
        print("Congratulations, " + name + "!")


def main():
    pass


if __name__ == '__main__':
    main()
