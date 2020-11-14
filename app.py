main_program = True


def program():
    print('Hello user, please enter a value to choose an option')
    print(
        'select 1 to find the sum of two number, 2 to find the product,'
        '3 to raise a number to a power, 4 to find the reminder,'
        'q for exit'
        )
    choice = input('please enter a value')

    global main_program
    while main_program:
        if(choice == '1'):
            print('1')
        elif(choice == '2'):
            print('2')
        elif(choice == '3'):
            print('3')
        elif(choice == '4'):
            print('4')
        elif(choice == 'q'):
            main_program = False
