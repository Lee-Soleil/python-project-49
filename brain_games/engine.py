import prompt


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    return name


def play(game):
    name = welcome_user()
    print(game.rules_of_the_game)
    count_round = 0
    while count_round < 3:
        question = game.get_question()
        correct_answer = game.get_correct_answer()
        print('Question: ' + str(question))
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
            if count_round == 2:
                print("Congratulations, " + name + "!")
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{str(correct_answer)}'")
            print("Let's try again, " + name + "!")
            break
        count_round += 1
