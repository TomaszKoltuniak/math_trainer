from inquirer import Text, List, Checkbox, prompt
from json import dump, load, decoder
from pandas import DataFrame
from time import sleep, time
from random import randint

LEADERBOARD_FILE_NAME = 'leaderboard.json'

menu_prompt = [
    Text('Name',
         message='Whats your name?',
         default='Annonymus'
         ),
    List('Difficulty',
         message='Choose the difficulty level:',
         choices=['Easy', 'Medium', 'Hard'],
         default='Easy'
         ),
    Checkbox('Operations',
             message='Choose the operations you wanna practice:',
             choices=['Addition', 'Subtraction', 'Multiplication', 'Division', 'Exponentiation', 'Roots',
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
        case 'Roots':
            match difficulty:
                case 'Easy':
                    increment = 3
                case 'Medium':
                    increment = 4
                case 'Hard':
                    increment = 5
                case _:
                    increment = 3
            a = randint(2, increment * 3)
            b = randint(2, increment)
            c = a ** b
            operator = '√'
            temp = a
            a = b
            b = c
            correct_result = temp
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
                'Answer': f'{a} {operator} {b} = {answer}, Correct result: {correct_result}'
                }


def main():
    print('''
Welcome to the Math Trainer! by Tomasz Kołtuniak
This program will help you practice your math skills.
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
        'Roots': {
            'Correct counter': 0,
            'Total Time': 0,
            'All Answers': [],
        },
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

    # Scoreboard
    total_correct_counter = 0
    total_time = 0
    total_all_answers = 0
    print(f"\n{settings['Name']}'s detailed Scoreboard:")
    for operation in settings['Operations']:
        total_correct_counter += score[operation]['Correct counter']
        total_time += score[operation]['Total Time']
        total_all_answers += len(score[operation]['All Answers'])
        success_rate = round(score[operation]['Correct counter'] / len(score[operation]['All Answers']) * 100)
        average_time = round(score[operation]['Total Time'] / len(score[operation]['All Answers']), 2)
        print(f'''
{operation}:
{success_rate}% - Success Rate
{average_time}s - Average Time
''')

    success_rate = round(total_correct_counter / total_all_answers, 2)
    average_time = round(total_time / total_all_answers, 2)

    # Leaderboard
    print('\n\n\nLeaderboard:')
    score = {
        'Success rate': success_rate,
        'Average time': average_time,
    }

    try:
        with open(LEADERBOARD_FILE_NAME, 'r') as file:
            leaderboard = load(file)
    except (FileNotFoundError, decoder.JSONDecodeError):
        leaderboard = {}

    name = settings['Name']

    if name in leaderboard:
        leaderboard[name]['Success rate'] = round((leaderboard[name]['Success rate'] + score['Success rate']) / 2, 2)
        leaderboard[name]['Average time'] = round((leaderboard[name]['Average time'] + score['Average time']) / 2, 2)
    else:
        leaderboard[name] = score

    with open(LEADERBOARD_FILE_NAME, 'w') as file:
        dump(leaderboard, file)

    table = DataFrame.from_dict(leaderboard, orient='index')
    sorted_table = table.sort_values(by='Success rate', ascending=False)
    print(sorted_table)


if __name__ == '__main__':
    main()

# Author: Tomasz Kołtuniak
# https://github.com/TomaszKoltuniak/math_trainer
