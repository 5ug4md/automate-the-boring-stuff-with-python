myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}


#ierating over each items in dictonary values
for s in myCat.values():
    print (s)

#ierating over each keys in dictonary 
for s in myCat.keys():
    print (s)
  
#iterating over key value pair both\   
for s in myCat.items():
    print (s)
    
    
#get method
print(myCat.get('size', 'not found'))
print(myCat.get('sizwe', 'not found'))


#setdefault method
#set default takes two arguement first is key and second is value
#it checks firstly if the key is present in the dictionary or not
#if it is in dictinoary it will return the value of that key
#else it will add new key value pair in the dictionary where key and value are two arguements in the setdefault method

myCat.setdefault('Age', '4')
