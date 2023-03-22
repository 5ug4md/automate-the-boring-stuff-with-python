while True: 
    age = input('enter your age: ')
    if age.isdecimal():
        break
    print("please enter a number for your age ")
while True:
    password = input("select a new password(letters and numbers only): ")
    if password.isalnum():
        break
    print("passwords can have letters and numbers only")