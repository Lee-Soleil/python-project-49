import prompt


COUNT_ROUND = 3


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    return name


def play(game):
    name = welcome_user()
    print(game.RULES_OF_THE_GAME)
    i = 1
    while i <= COUNT_ROUND:
        question, correct_answer = game.generate_question_answer()
        print('Question: ' + str(question))
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{str(correct_answer)}'.\n"
                  f"Let's try again, " + name + "!")
            break
        if i == COUNT_ROUND and answer == correct_answer:
            print("Congratulations, " + name + "!")
        i += 1
