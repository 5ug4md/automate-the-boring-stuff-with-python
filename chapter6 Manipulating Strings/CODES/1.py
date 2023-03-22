# Escape character in python


# \ to escape a character
# \t for a tab
# \n for a new line


print('Hello!,\tHow are you?\nI\'m Doing fine')


# we can use raw string to ignore the escape character and print it too
print(r'Hello!,\tHow are you?\nI\'m Doing fine')


# use triple single or double quotes for multiline strings

print("""
      hello
      world
      this
      is multiline
      strings
      in python
      """)

#we can use """ for multiline comments too
"""just some random comments
    new line 
    lel
    """


#useful string methods

#    upper(),lower(),issuper(), islower()

text = 'elon'
text1 = 'ElOn'
print(text.upper())
print(text1.lower())

print(text.isupper())
print(text1.isupper())

print(text.islower())
print(text1.islower())


"""
isalpha() Returns True if the string consists only of letters and isn’t blank

isalnum() Returns True if the string consists only of letters and numbers and is not blank

isdecimal() Returns True if the string consists only of numeric characters and is not blank

isspace() Returns True if the string consists only of spaces, tabs, and newlines and is not blank

istitle() Returns True if the string consists only of words that begin with an uppercase letter followed by only lowercase letters
"""


