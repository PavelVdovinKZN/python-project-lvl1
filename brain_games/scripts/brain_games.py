import prompt


def name():
    print("Welcome to the Brain Games!")
    name1 = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name1))


if __name__ == '__main__':
    name()
