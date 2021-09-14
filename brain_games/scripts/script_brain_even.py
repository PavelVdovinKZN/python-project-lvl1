#!/usr/bin/env python

from brain_games.games import brain_even
from brain_games.common_logic import engine_of_games


def main():
    engine_of_games(brain_even)


if __name__ == "__main__":
    main()
