from random import randint


rules_of_the_game = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question():
    global random_number
    random_number = randint(1, 50)
    question = random_number
    return question


def get_correct_answer():
    if random_number == 1:
        return 'no'
    for i in range(2, (random_number // 2) + 1):
        if random_number % i == 0:
            return 'no'
    return 'yes'
