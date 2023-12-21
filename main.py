from inquirer import Text, List, Checkbox, prompt
from random import randint
from time import sleep, time

menu_prompt = [
    Text('Name',
         message='Whats your name?',
         default='Anonymous'
         ),
    List('Difficulty',
         message='Choose the difficulty level:',
         choices=['Easy', 'Medium', 'Hard'],
         default='Easy'
         ),
    Checkbox('Operations',
             message='Choose the operations you wanna practice:',
             choices=['Addition', 'Subtraction', 'Multiplication', 'Division', 'Exponentiation', 'Roots',
                      'Logarithms'],
             ),
]

keep_playing_prompt = [
    List('continue',
         message='Do you want to continue?:',
         choices=['Continue', 'Exit'],
         default='Continue'
         ),
]


def calculation(operation, difficulty):
    a = randint(1, 10 ** difficulty)
    b = randint(1, 10 ** difficulty)
    match operation:
        case 'Addition':
            operator = '+'
            correct_result = a + b
        case 'Subtraction':
            operator = '-'
            correct_result = a - b
        case 'Multiplication':
            operator = '*'
            correct_result = a * b
        case 'Division':
            operator = '/'
            correct_result = a / b
        case 'Exponentiation':
            operator = '**'
            correct_result = a ** b
        case 'Roots':
            operator = '√'
            correct_result = a ** (1 / b)
        case 'Logarithms':
            operator = 'log'
            correct_result = a ** (1 / b)
        case _:
            print('Error: Unknown operation')
            return 'Error: Unknown operation'

    start_time = time()
    answer = int(input(f'{a} {operator} {b} = '))
    end_time = time()
    stopwatch = end_time - start_time
    if correct_result == answer:
        print('\033[92mCorrect!\033[0m')
        return f'Correct {a} {operator} {b} = {answer}'
    else:
        print('\033[91mIncorrect!\033[0m')
        return f'Incorrect {a} {operator} {b} = {answer} should be {correct_result}'


def main():
    print('''
Welcome to the Math Trainer! by Tomasz Kołtuniak
This program will help you practice your math skills.
Choose the difficulty level:
    ''')

    settings = prompt(menu_prompt)
    match settings['Difficulty']:
        case 'Easy':
            difficulty = 1
        case 'Medium':
            difficulty = 2
        case 'Hard':
            difficulty = 3
        case _:
            difficulty = 1
    score = {
        'Addition': [],
        'Subtraction': [],
        'Multiplication': [],
        'Division': [],
        'Exponentiation': [],
        'Roots': [],
        'Logarithms': [],
    }

    keep_playing = {'continue': 'Continue'}
    while keep_playing['continue'] == 'Continue':
        for operation in settings['Operations']:
            score[operation].append(calculation(operation, difficulty))

        keep_playing = prompt(keep_playing_prompt)

    print('\nScoreboard:')
    for operation in settings['Operations']:
        print(f'\n{operation}:')
        for result in score[operation]:
            print(result)


if __name__ == '__main__':
    main()
