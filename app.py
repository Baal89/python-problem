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
    if(choice == '1'):
        # cambiato qua
        sum_of_numbers(*get_information())

    elif(choice == '2'):
        # aggiunto -1 e print
        print(product_of_numbers(*get_information())-1)

    elif(choice == '3'):
        # aggiunto print
        print(esponent_of_numbers(*get_information()))

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
            # qua ho aggiunto questo pezzo cosi non si possono mettere valori negativi! top.
            if (x < 0 or y < 0):
                raise ValueError
            break
        except ValueError:
            print('my processors cannot understand the inputs')
    return x, y


def sum_of_numbers(x, y):
    # messo solo return
    sum = x + y
    print('Calculation succed the result is: ' + str(sum))
    program()


# questa funzione e` cambiata molto
def product_of_numbers(x, y):
    if(x < y):
        return product_of_numbers(y, x)
    if(x == 0):
        print('first value is equal to 0, result: ', x * y)
        return 1
    else:
        if(y == 0):
            print('End of calculation')
            return 1
        else:
            res = x + product_of_numbers(x, y - 1)
            return res


# anche questa
def esponent_of_numbers(x, y):
    if(y == 0):
        print('End of calculation')
        return 1
    elif(y % 2 == 0):
        res = esponent_of_numbers(x, y / 2)**2
        return res
    else:
        res = x * esponent_of_numbers(x, y - 1)
        return res


# sopratutto questa
def modulo_of_numbers(x, y):
    if(x < y):
        print('End of calculation')
        print('The result is: ', x)
        return 1
    if(y < x):
        res = modulo_of_numbers(x - y, y)
        return res


# questo pezzettino qua serve a non chiamare main program tutte le volte
# nelle altre funzioni
while main_program:
    program()


program()
