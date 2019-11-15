def say_hello(name):
    print("Hello, " + name)

    say_hello()

answer = input("Would you like another greeting?")
if answer == 'y':
    say_hello()