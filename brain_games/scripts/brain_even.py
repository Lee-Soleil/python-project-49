#!/usr/bin/env python3

import prompt
from random import randint


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    while i < 3:
        random_number = randint(1, 100)
        print('Question: ' + str(random_number))
        answer = prompt.string('Your answer: ')
        if random_number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        if (random_number % 2 == 0 and answer == 'yes') or (random_number % 2 != 0 and answer == 'no'):
            print('Correct!')
            if i == 2:
                print("Congratulations, " + name + "!")
        else:
            print("'" + answer + "' is wrong answer ;(. Correct answer was '" + correct_answer + "'.")
            print("Let's try again, " + name + "!")
            break
        i += 1


if __name__ == '__main__':
    main()
