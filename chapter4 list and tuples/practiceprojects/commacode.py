
def commacode(lst):
        if len(lst) == 0:
            return ''
        elif len(lst) == 1:
            return lst[0]
        else:
            return ', '.join(lst[:-1]) + ', and ' + lst[-1]
        
spam = ['apples', 'bananas', 'tofu', 'cats']
formatted = commacode(spam)
print(formatted)