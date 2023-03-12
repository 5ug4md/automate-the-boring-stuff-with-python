import random

randomNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')

for geussTaken in range(1, 7):

    print('Take a guess.')
    guess = int(input())
    if guess < randomNumber:
        print('Your guess is too low.')
    elif guess > randomNumber:
        print('Your guess is too high.')
    else:
        break

if guess == randomNumber:
    print("Good job! You guessed my number in " + str(geussTaken) + " guesses!")
else:
    print("you missed all your 6 chances")
    print("the number was " + str(randomNumber))
