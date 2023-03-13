import random
occurance = []
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    num = int(random.randint(0, 1))
    if num == 0:
        occurance.append('H')
    else:
        occurance.append('T')

# Code that checks if there is a streak of 6 heads or tails in a row.
def six_H_or_T_in_a_row(lst):
    numberOfStreaks = 0
    for i in range(len(lst) - 5):
        if lst[i:i+6] == ['H', 'H', 'H', 'H', 'H', 'H'] or lst[i:i+6] == ['T', 'T', 'T', 'T', 'T', 'T']:
            numberOfStreaks += 1
    return numberOfStreaks


numberOfStreaks = six_H_or_T_in_a_row(occurance)
print(numberOfStreaks)
print('Chance of streak: %s%%' % (numberOfStreaks / 100))
