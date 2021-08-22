import prompt


def name():
    name = prompt.string('May i have your name? ')
    return name


if __name__ == "__main__":
    name()
