from random import randint
from random import choice


rules_of_the_game = 'What is the result of the expression?'


def get_question():
    global random_number_one, random_number_two, operation
    random_number_one = randint(1, 10)
    random_number_two = randint(1, 10)
    operation = ''.join(choice('+-*') for i in range(1))
    question = str(random_number_one) + ' ' + operation + ' ' + str(random_number_two)
    return question


def get_correct_answer():
    if operation == '+':
        correct_answer = str(random_number_one + random_number_two)
    elif operation == '-':
        correct_answer = str(random_number_one - random_number_two)
    elif operation == '*':
        correct_answer = str(random_number_one * random_number_two)
    return correct_answer
