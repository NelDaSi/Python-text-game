def add(arg1, arg2):
    print(str("The result is: ") + str(int(arg1) + int(arg2)))


while True:
    print("\n Type 2 numbers to added together!")
    try:
        first = input('\t First number: \n> ')
        second = input('\t Second number: \n> ')

        add(first, second)
    except ValueError:
        print('Oeps, something as gone terrably wrong. '
              + 'Try again.')
