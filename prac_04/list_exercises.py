def list_exercise():
    numbers = []
    for i in range(5):
        number = int(input('Enter a number: '))
        numbers.append(number)
    numbers.sort()
    sum_numbers = sum(numbers)
    avg_numbers = sum(numbers) / 5
    print('min is {}'.format(numbers[0]))
    print('max is {}'.format(numbers[4]))
    print('sum is {}'.format(sum_numbers))
    print('len of numbers {}'.format(len(numbers)))
    print('average number is {}'.format(avg_numbers))

    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    get_usernames = str(input('usernames: '))
    if get_usernames in usernames:
        print('Access granted')
    else:
        print("Access denied")


list_exercise()
