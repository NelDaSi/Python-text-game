# print("How old are you?")
# user_input = input(">")
# user_age = int(user_input)
age = int(input("How old are you?\n>"))
if age >= 18:
    print("\nYou are aloud to vote!")
elif age == 17:
    print("\nYou are almost an adult.")
elif age <= 16:
    print("\nYou can drive a car, \n\t But can`t drink alcohol! ")
else:
    print("\nThat`s not a number!")
