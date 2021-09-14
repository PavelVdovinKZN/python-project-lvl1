#!/usr/bin/env python
from random import randint, choice
import operator

TASK_DESCRIPTION = 'What is the result of the expression?'
FIRST_NUMBER = 1
SECOND_NUMBER = 10

operators = {
    '+': operator.add,
    '*': operator.mul,
    "-": operator.sub,
}
operator_symbols = list(operators.keys())


def game_round():
    num1 = randint(FIRST_NUMBER, SECOND_NUMBER)
    num2 = randint(FIRST_NUMBER, SECOND_NUMBER)
    operator_symbol = choice(operator_symbols)
    current_operator = operators.get(operator_symbol)
    question = (str(num1) + operator_symbol + str(num2))
    return question, str(current_operator(num1, num2))
