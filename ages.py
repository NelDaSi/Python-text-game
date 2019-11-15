print ("How old are you?")
user_input = input(">")
user_age = int(user_input)
#user_age = print(input("How old are you: \n >"))
#user_age = int(user_input)
if user_age >= 18:
    print ("You are aloud to vote!")
elif user_age == 17:
    print ("You are almost an adult.")
elif user_age <= 16:
    print ("You can drive a car, \n\t But can`t drink alcohol! ")
else:
    print("That`s not a number!")
