from random import randint


RULES_OF_THE_GAME = 'Answer "yes" if given number \
is prime. Otherwise answer "no".'


def is_prime(x):
    if x == 1:
        return False
    for i in range(2, (x // 2) + 1):
        if x % i == 0:
            return False
    return True


def generate_question_answer():
    random_number = randint(1, 50)
    question = random_number
    if is_prime(random_number):
        return question, 'yes'
    else:
        return question, 'no'
