from random import randint
from random import choice


RULES_OF_THE_GAME = 'What is the result of the expression?'


def generate_question_answer():
    a = randint(1, 10)
    b = randint(1, 10)
    operation = ''.join(choice('+-*') for i in range(1))
    question = (f'{str(a)} {operation} {str(b)}')
    if operation == '+':
        correct_answer = a + b
    elif operation == '-':
        correct_answer = a - b
    elif operation == '*':
        correct_answer = a * b
    return question, str(correct_answer)
