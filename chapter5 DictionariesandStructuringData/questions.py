#1 What does the code for empty dictionary look like?
# {}


#2 What does a dictionary value with a key 'foo' and a value 42 look like?
# {'foo': 42}

#3 What is the main difference between a dictionary and a list?
# Dictonaries are unordered, while lists are ordered. Dictionary keys are unique, while list items are not. Dictionaries are accessed by keys, while lists are accessed by their index.


#4 What happens if you try to access spam['foo'] if spam is {'bar': 100}?
# KeyError: 'foo'

#5 If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.keys()?
# 'cat' in spam checks if there is a 'cat' key in the dictionary, while 'cat' in spam.keys() checks if there is a value 'cat' for one of the keys in the dictionary.

#6 If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.values()?
# cat in spam checks if there is a 'cat' key in the dictionary, while 'cat' in spam.values() checks if there is a value 'cat' for one of the values in the dictionary.


#7 What is a shortcut for the following code?
# if 'color' not in spam:
#    spam['color'] = 'black'

# spam.setdefault('color', 'black')

#8 How do you "pretty print" dictionary values using which module and function?
#pprint.pprint()