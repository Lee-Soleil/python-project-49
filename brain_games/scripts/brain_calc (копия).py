#!/usr/bin/env python3

import prompt
from random import randint
from random import choice


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('What is the result of the expression?')
    i = 0
    while i < 3:
        random_number_one = randint(1, 10)
        random_number_two = randint(1, 10)
        operation = ''.join(choice('+-*') for i in range(1))
        if operation == '+':
            correct_answer = random_number_one + random_number_two
        elif operation == '-':
            correct_answer = random_number_one - random_number_two
        elif operation == '*':
            correct_answer = random_number_one * random_number_two
        print('Question: ' + str(random_number_one) + operation + str(random_number_two))
        answer = prompt.string('Your answer: ')
        if correct_answer == int(answer):
            print('Correct!')
            if i == 2:
                print("Congratulations, " + name + "!")
        else:
            print("'" + answer + "' is wrong answer ;(. Correct answer was '" + str(correct_answer) + "'.")
            print("Let's try again, " + name + "!")
            break
        i += 1


if __name__ == '__main__':
    main()
