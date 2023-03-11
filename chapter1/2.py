name = ''


while name != 'your name':
    print('Please type your name.')
    name = input()
print('Thank you!')

# When used in conditions, 0, 0.0, and '' (the empty string) are considered False,
while not name:
    print('Please type your name.')
    name = input()
print('Thank you!')

while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello, Joe. What is the password? (It is a fish.)')
    password = input()
    if password == 'swordfish':
        break
print('Access granted.')
