import prompt


def name():
    name_user = prompt.string('May i have your name? ')
    return name_user


if __name__ == "__main__":
    name()
