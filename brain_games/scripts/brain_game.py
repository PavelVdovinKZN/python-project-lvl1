#!/usr/bin/env python

import prompt


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May a have your name? ')
    print('Hello, {0}'.format(name))


if __name__ == '__main__':
    main()
