def welcome():
    print('''
Welcome to My First Calculator Project
''')
...
def calculate():
    operation = input('''   
        Enter the math operation you would like to complete:
        + for addition
         - for subtraction
         * for multiplication
         / for division

        ''')

    num_1 = int(input('Enter your first number: '))
    num_2 = int(input('Enter your second number: '))

    print('{} + {} = '.format(num_1, num_2))
    print(num_1 + num_2)

    if operation == '+':
        print('{} + {} = '.format(num_1, num_2))
        print(num_1 + num_2)

    elif operation == '-':
        print('{} - {} = '.format(num_1, num_2))
        print(num_1 - num_2)

    elif operation == '*':
        print('{} * {} = '.format(num_1, num_2))
        print(num_1 * num_2)

    elif operation == '/':
        print('{} / {} = '.format(num_1, num_2))
        print(num_1 / num_2)
    else:
        print('You have not typed a valid operator. Please run the program again')
def again():

    # Take input from user
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
''')

    # # Accept 'y' or 'Y' by adding str.upper()
    if calc_again.upper() == 'Y':
        calculate()

    # Accept 'n' or 'N' by adding str.upper()
    elif calc_again.upper() == 'N':
        print('See you later.')

    else:
        again()
welcome()
calculate()
again()
