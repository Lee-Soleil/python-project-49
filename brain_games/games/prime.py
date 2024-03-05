from random import randint


rules_of_the_game = 'Answer "yes" if given number \
is prime. Otherwise answer "no".'


def generate_question_answer():
    random_number = randint(1, 50)
    question = random_number
    if random_number == 1:
        return question, 'no'
    for i in range(2, (random_number // 2) + 1):
        if random_number % i == 0:
            return question, 'no'
    return question, 'yes'
