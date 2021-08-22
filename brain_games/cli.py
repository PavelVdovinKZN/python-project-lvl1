import prompt


def name():
    name_user = prompt.string('May i have your name? ')
    print('Hello, {0}!'.format(name))
    return name_user


if __name__ == "__main__":
    name()
