import pprint
message = input("Enter a message: ")

counts = {}

for character in message:
    counts.setdefault(character, 0)
    counts[character] = counts[character] + 1
    
pprint.pprint(counts)