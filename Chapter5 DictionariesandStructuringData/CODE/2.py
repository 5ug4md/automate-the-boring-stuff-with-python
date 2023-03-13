birthdays = {'sugam': 'march 23', 'aaku': 'jan 27', 'raju':'nov 1'}


while True:
    print('Enter a name(blank to quit): ')
    name = input()
    if name == '':
        break
    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
        print()
        print()
    else:
        print("birthday not in database for " + name)
        print("when is your birthday?")
        bday = input()
        birthdays[name] = bday
        print("birthday database updated")
        