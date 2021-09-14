#!/usr/bin/env python
import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    return name


if __name__ == "__main__":
    welcome_user()
