import prompt


COUNT_ROUND = 1


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    return name


def play(game):
    name = welcome_user()
    print(game.rules_of_the_game)
    COUNT_ROUND = 1
    while COUNT_ROUND <= 3:
        question = game.get_question()
        correct_answer = game.get_correct_answer()
        print('Question: ' + str(question))
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{str(correct_answer)}'.\n"
                  f"Let's try again, " + name + "!")
            break
        if COUNT_ROUND == 3 and answer == correct_answer:
            print("Congratulations, " + name + "!")
        COUNT_ROUND += 1
