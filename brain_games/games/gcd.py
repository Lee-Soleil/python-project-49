from random import randint


rules_of_the_game = 'Find the greatest common divisor of given numbers.'


def generate_question_answer():
    random_number_one = randint(1, 50)
    random_number_two = randint(1, 50)
    question = str(random_number_one) + ' ' + str(random_number_two)
    while random_number_one != random_number_two:
        if random_number_one > random_number_two:
            random_number_one = random_number_one - random_number_two
        else:
            random_number_two = random_number_two - random_number_one
    correct_answer = str(random_number_one)
    return question, correct_answer
