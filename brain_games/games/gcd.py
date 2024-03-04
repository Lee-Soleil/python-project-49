from random import randint


rules_of_the_game = 'Find the greatest common divisor of given numbers.'


def get_question():
    global random_number_one, random_number_two
    random_number_one = randint(1, 50)
    random_number_two = randint(1, 50)
    question = str(random_number_one) + ' ' + str(random_number_two)
    return question


def get_denominator_one(random_number):
    divider = []
    for i in range(1, random_number + 1):
        if random_number % i == 0:
            divider.append(i)
        i += 1
    return divider


def compare_deviders(divider_o, divider_t):
    dividers = []
    for item_one in divider_o:
        if item_one in divider_t:
            dividers.append(item_one)
    return dividers


def get_correct_answer():
    divider_one = get_denominator_one(random_number_one)
    divider_two = get_denominator_one(random_number_two)
    dividers = compare_deviders(divider_one, divider_two)
    dividers.sort(reverse=True)
    correct_answer = str(dividers[0])
    return correct_answer
