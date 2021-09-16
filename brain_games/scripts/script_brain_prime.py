#!/usr/bin/env python

from brain_games.games import brain_prime
from brain_games.common_logic import get_engine_of_games


def main():
    get_engine_of_games(brain_prime)


if __name__ == "__main__":
    main()
