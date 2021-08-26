#!/usr/bin/env python
import prompt


def name_user():
    name_us = prompt.string('May I have your name? ')
    print('Hello, {0}'.format(name_us))
    return name_us


def welcome_user():
    return print("Welcome to the Brain Games!")


# if __name__ == "__main__":
#     main()
