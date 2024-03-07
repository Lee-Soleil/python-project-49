from random import randint


RULES_OF_THE_GAME = 'Find the greatest common divisor of given numbers.'


def gcd(x, y):
    while x != y:
        if x > y:
            x = x - y
        else:
            y = y - x
    return x


def generate_question_answer():
    a = randint(1, 50)
    b = randint(1, 50)
    question = str(a) + ' ' + str(b)
    correct_answer = str(gcd(a, b))
    return question, correct_answer
