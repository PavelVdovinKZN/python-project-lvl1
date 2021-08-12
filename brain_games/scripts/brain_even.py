import random

import prompt


def main():
    check_play = 0
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    print("Answer \"yes\" if the number is even, otherwise answer \"no\".")
    while int(check_play) < 3:
        rand_num = random.randint(0, 100)
        print("Question: " + str(rand_num))
        if rand_num % 2 == 0:
            correct_answer = "yes"
        else:
            correct_answer = "no"
        user_answer = input('Your answer: ')
        if rand_num % 2 == 0 and user_answer == "yes" or rand_num % 2 > 0 and user_answer == "no":
            print("Correct!")
            check_play += 1
            if int(check_play) == 3:
                print("Congratulations, {0}!".format(name))
                return True
        else:
            print("'" + user_answer + "' is wrong answer ;(. Correct answer was "
                  + "'" + correct_answer + "'" ".\nLet's try again, {0}!".format(name))
            return False


if __name__ == '__main__':
    main()
