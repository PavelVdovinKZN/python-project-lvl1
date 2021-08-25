import random
import sys

from brain_games.scripts.brain import name_user, welcome_user

welcome = welcome_user()
name_us = name_user()


def even():
    print("Answer \"yes\" if the number is even, otherwise answer \"no\".")
    for i in range(3):
        rand_num = random.randint(0, 100)
        print("Question: " + str(rand_num))
        if rand_num % 2 == 0:
            correct_answer = "yes"
        else:
            correct_answer = "no"
        user_answer = input('Your answer: ')
        if user_answer == correct_answer:
            print("Correct!")
            i += 1
        else:
            print(
                "\'{0}\' is wrong answer ;(.Correct answer was \'{1}{2}".format(
                    str(user_answer), str(correct_answer),
                    "'" ".\nLet's try again, {0}!".format(name_us)))
            sys.exit()


even()

print("Congratulations, {0}!".format(name_us))


def main():
    pass


if __name__ == '__main__':
    main()
