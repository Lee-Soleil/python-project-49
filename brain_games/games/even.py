from random import randint


rules_of_the_game = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question():
    global random_number
    random_number = randint(1, 100)
    question = random_number
    return question


def get_correct_answer():
    if random_number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer
