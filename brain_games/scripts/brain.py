#!/usr/bin/env python
import prompt


def welcome_user():
    return print("Welcome to the Brain Games!")


def name_user():
    name_us = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name_us))
    return name_us


# if __name__ == "__main__":
#     main()
