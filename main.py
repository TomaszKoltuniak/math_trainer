from inquirer import Text, List, Checkbox, prompt
from random import randint
from time import sleep, time

menu_prompt = [
    Text('Name',
         message='Whats your name?',
         default='John'
         ),
    List('Difficulty',
         message='Choose the difficulty level:',
         choices=['Easy', 'Medium', 'Hard'],
         default='Easy'
         ),
    Checkbox('Operations',
             message='Choose the operations you wanna practice:',
             choices=['Addition', 'Subtraction', 'Multiplication', 'Division', 'Exponentiation',
                      # 'Roots',
                      # 'Logarithms'
                      ],
             ),
]

keep_playing_prompt = [
    List('Continue',
         message='Do you want to continue?:',
         choices=['Continue', 'Exit'],
         default='Continue'
         ),
]


def calculation(operation, difficulty):
    a = randint(1, 10 ** difficulty)
    b = randint(1, 10 ** difficulty)
    c = randint(1, 10 ** difficulty)
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
            a = b * c
            correct_result = c
        case 'Exponentiation':
            operator = '**'
            correct_result = a ** b
        # case 'Roots':
        #     operator = '√'
        #     correct_result = a ** (1 / b)
        # case 'Logarithms':
        #     operator = 'log'
        #     correct_result = a ** (1 / b)
        case _:
            print('Error: Unknown operation')
            return 'Error: Unknown operation'

    start_time = time()
    answer = int(input(f'{a} {operator} {b} = '))
    end_time = time()
    stopwatch = end_time - start_time
    if correct_result == answer:
        print('\033[92mCorrect!\033[0m')
        return {'Correct': 1,
                'Time': stopwatch,
                'Answer': f'{a} {operator} {b} = {answer}'
                }
    else:
        print('\033[91mIncorrect!\033[0m')
        print(f'Correct result is {correct_result}')
        return {'Correct': 0,
                'Time': stopwatch,
                'Answer': f'{a} {operator} {b} = {answer}, Correct answer: {correct_result}'
                }


def main():
    print('''
Welcome to the Math Trainer! by Tomasz Kołtuniak
This program will help you practice your math skills.
Choose the difficulty level:
    ''')

    settings = prompt(menu_prompt)

    for timer in range(5, 0, -1):
        print(f'\rStarting in {timer} seconds...', end='')
        sleep(1)

    print('\n\nGood luck!\n\n')

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
        'Addition': {
            'Correct counter': 0,
            'Total Time': 0,
            'All Answers': [],
        },
        'Subtraction': {
            'Correct counter': 0,
            'Total Time': 0,
            'All Answers': [],
        },
        'Multiplication': {
            'Correct counter': 0,
            'Total Time': 0,
            'All Answers': [],
        },
        'Division': {
            'Correct counter': 0,
            'Total Time': 0,
            'All Answers': [],
        },
        'Exponentiation': {
            'Correct counter': 0,
            'Total Time': 0,
            'All Answers': [],
        },
        # 'Roots': {
        #     'Correct counter': 0,
        #     'Total Time': 0,
        #     'All Answers': [],
        # },
        # 'Logarithms': {
        #     'Correct counter': 0,
        #     'Total Time': 0,
        #     'All Answers': [],
        # },
    }

    keep_playing = {'Continue': 'Continue'}
    while keep_playing['Continue'] == 'Continue':
        for operation in settings['Operations']:
            result = calculation(operation, difficulty)
            score[operation]['Correct counter'] += result['Correct']
            score[operation]['Total Time'] += result['Time']
            score[operation]['All Answers'].append(result['Answer'])

        keep_playing = prompt(keep_playing_prompt)

    print(f"\n{settings['Name']}'s Scoreboard:")
    for operation in settings['Operations']:
        success_rate = round(score[operation]['Correct counter'] / len(score[operation]['All Answers']) * 100)
        average_time = round(score[operation]['Total Time'] / len(score[operation]['All Answers']), 1)
        print(f'''
{operation}:
{success_rate}% - Success Rate
{average_time}s - Average Time
Cya!
''')


if __name__ == '__main__':
    main()
