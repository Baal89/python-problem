main_program = True


def program():
    print('Hello user, please enter a value to choose an option')
    print('select 1 to find the sum of two number')
    print('select 2 to find the product two number')
    print('select 3 to raise a number to a power')
    print('4 to find the reminder two number')
    print('select q for exit')

    choice = input('human enter a value: ')

    global main_program
    while main_program:
        if(choice == '1'):
            sum_of_numbers()

        elif(choice == '2'):
            product_of_numbers(*get_information())

        elif(choice == '3'):
            esponent_of_numbers(*get_information())

        elif(choice == '4'):
            modulo_of_numbers(*get_information())

        elif(choice == 'q'):
            print('program terminated')
            main_program = False
        else:
            print('wrong value entered')


def get_information():
    while True:
        try:
            x = float(input('human enter a value: '))
            y = float(input('human enter second value: '))
            return x, y
        except ValueError:
            print('my processors cannot understand the inputs')


def sum_of_numbers():
    x, y = get_information()
    sum = x + y
    print(sum)
    program()


def product_of_numbers(x, y):
    if(x < y):
        print(product_of_numbers(y, x))
        program()
    if(x == 0):
        print(0)
        program()
    else:
        print(x + product_of_numbers(x, y-1))
        program()


def esponent_of_numbers(x, y):
    if y == 0:
        print(1)
        program()
    elif y % 2 == 0:
        print(esponent_of_numbers(x, y / 2)**2)
        program()
    else:
        print(x * esponent_of_numbers(x, y-1))
        program()


def modulo_of_numbers(x, y):
    if x < y:
        print(x)
    print(modulo_of_numbers(x - y, y))
    program()


program()
