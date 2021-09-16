#!/usr/bin/env python

from brain_games.games import brain_progression
from brain_games.common_logic import get_engine_of_games


def main():
    get_engine_of_games(brain_progression)


if __name__ == "__main__":
    main()
