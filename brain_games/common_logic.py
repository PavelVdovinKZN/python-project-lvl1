#!/usr/bin/env python
import prompt
COUNT_ROUNDS = 3


def welcome():
    print("Welcome to the Brain Games!")


def get_user_name():
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    return user_name


def get_engine_of_games(game):
    welcome()
    user_name = get_user_name()
    print(game.TASK_DESCRIPTION)
    for i in range(COUNT_ROUNDS):
        question, correct_answer = game.get_game_round()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'\n"
                f"Let's try again, {user_name}!"
            )
            return
    print(f'Congratulations, {user_name}!')
