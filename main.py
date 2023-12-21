import inquirer


def main():
    print('''
Welcome to the Math Trainer! by Tomasz Kołtuniak
This program will help you practice your math skills.
Choose the difficulty level:
    ''')

    settings = [
        inquirer.Text('name',
                      message='Whats your name?',
                      default='Anonymous'),
        inquirer.List('difficulty',
                      message='Choose the difficulty level:',
                      choices=['Easy', 'Medium', 'Hard'],
                      ),
        inquirer.Checkbox('operations',
                          message='Choose the operations you wanna practice:',
                          choices=['Addition', 'Subtraction', 'Multiplication', 'Division', 'Exponentiation', 'Roots',
                                   'Logarithms'],
                          ),
    ]
    answers = inquirer.prompt(settings)
    print(answers)


if __name__ == '__main__':
    main()
