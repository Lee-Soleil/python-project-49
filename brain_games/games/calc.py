from random import randint
from random import choice


rules_of_the_game = 'What is the result of the expression?'


def generate_question_answer():
    random_number_one = randint(1, 10)
    random_number_two = randint(1, 10)
    operation = ''.join(choice('+-*') for i in range(1))
    question = (str(random_number_one) + ' ' + operation
                + ' ' + str(random_number_two))
    if operation == '+':
        correct_answer = str(random_number_one + random_number_two)
    elif operation == '-':
        correct_answer = str(random_number_one - random_number_two)
    elif operation == '*':
        correct_answer = str(random_number_one * random_number_two)
    return question, correct_answer
