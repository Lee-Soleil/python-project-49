from random import randint


rules_of_the_game = 'Find the greatest common divisor of given numbers.'


def get_question():
    global random_number_one, random_number_two
    random_number_one = randint(1, 50)
    random_number_two = randint(1, 50)
    question = str(random_number_one) + ' ' + str(random_number_two)
    return question


def get_correct_answer():
    denominator_one = []
    for i in range(1, random_number_one + 1):
        if random_number_one % i == 0:
            denominator_one.append(i)
        i += 1
    denominator_two = []
    for i in range(1, random_number_two + 1):
        if random_number_two % i == 0:
            denominator_two.append(i)
        i += 1
    denominators = []
    for item_one in denominator_one:
        for item_two in denominator_two:
            if item_one == item_two:
                denominators.append(item_one)
    denominators.sort(reverse=True)
    correct_answer = str(denominators[0])
    return correct_answer
