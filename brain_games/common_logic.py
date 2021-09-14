#!/usr/bin/env python

COUNT_ROUNDS = 3


def welcome():
    print("Welcome to the Brain Games!")


def name_us():
    name_user = input(str('May I have your name? '))
    print('Hello, ' + name_user + "!")
    return name_user


def engine_of_games(game):
    welcome()
    name_user = name_us()
    print(game.TASK_DESCRIPTION)
    for i in range(COUNT_ROUNDS):
        question, correct_answer = game.game_round()
        print('Question: ' + question)
        user_answer = input(str('Your answer: '))
        if user_answer == correct_answer:
            print('Correct!')
        else:
            print("'" + str(user_answer) + "' is wrong answer ;(. "
                                           "Correct answer was '" + str(
                correct_answer) + "'.\nLet's try again, " + name_user + '!')
            return
    print("Congratulations, " + name_user + "!")
