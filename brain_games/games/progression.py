from random import randint


rules_of_the_game = 'What number is missing in the progression?'


def generate_question_answer():
    # начало прогрессии
    start_progression = randint(1, 40)
    # длина прогрессии
    lenght_progression = randint(4, 9)
    # шаг прогрессии
    step_progression = randint(1, 10)
    # конец прогрессии
    end_progression = start_progression + lenght_progression * step_progression
    # номер неизвестного числа в прогрессии
    unknown_progression = randint(1, lenght_progression - 1)
    # само неивестное
    unknown_number = start_progression + unknown_progression * step_progression
    full_progression = ''
    for i in range(start_progression, unknown_number, step_progression):
        full_progression = full_progression + str(i) + ' '
    full_progression = full_progression + '.. '
    for i in range(unknown_number + step_progression,
                   end_progression + 1, step_progression):
        full_progression = full_progression + str(i) + ' '
    question = full_progression
    correct_answer = str(unknown_number)
    return question, correct_answer
