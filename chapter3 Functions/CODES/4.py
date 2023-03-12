import time

def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(3 * number + 1)
        return 3 * number + 1

try:
    input = int(input("enter a number: "))
    while input != 1:
        input = collatz(input)
        time.sleep(0.1)
except ValueError:
    print('Please enter an integer.')   