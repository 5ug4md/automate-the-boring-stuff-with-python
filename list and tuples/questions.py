#1 what is []
# [ ] is a list


#2. how would you assign the value 'hello' as the third value in a list stored in a variable called spam? (Assume spam contains [2, 4, 6, 8, 10].) For the next three questions, let’s say spam contains the list ['a', 'b', 'c', 'd'].
spam = [2, 4, 6, 8, 10]
spam.insert(2, 'hello')
print(spam)

#3. what does spam[int(int('3' * 2)//11)] evaluate to?
# 'd' i.e spam[3] 
print(spam[int(int('3' * 2)//11)])

#4. what does spam[-1] evaluate to?
# last item of the list
print(spam[-1])

#5. what does spam[:2] evaluate to?
# displays items of list from 0 to 2

print(spam[:2])


#let's pretend bacon has the list [3.14, 'cat', 11, 'cat', True] for the next three questions, 
bacon = [3.14, 'cat', 11, 'cat', True]

#6 what does bacon.index('cat') evaluate to?
#index of cat i.e 1
print(bacon.index('cat'))

#7. what does bacon.append(99) make the list value in bacon look like?
# adds 99 to the end of the list
bacon.append(99)
print(bacon)


#8. what does bacon.remove('cat') make the list value in bacon look like?
#removes cat that occurs first in the list
bacon.remove('cat')
print(bacon)

#9 what are the operators for list concatenation and list replication?
# + and *

#10. what is the difference between the append() and insert() list methods?
# append adds to the end of the list while insert adds to a specific index

#11. what are two ways to remove values from a list?
# del statement and remove() method

#12. name a few ways that list values are similar to string values.
# both can be indexed and sliced

#13. what is the difference between lists and tuples?
# lists are mutable while tuples are immutable

#14. how do you type the tuple value that has just the integer value 42 in it?
TuplE= (42,)

# 15. how can you get the tuple form of a list value? how can you get the list form of a tuple value?
# tuple(list) and list(tuple)  respectively

#16. variables that “contain” list values don’t actually contain lists directly. what do they contain instead?
# they contain references to list values

#17. what is the difference between copy.copy() and copy.deepcopy()?
# copy.copy() does a shallow copy of a list i.e modifying copy also modifies the orginal list while copy.deepcopy() does a deep copy of a list i.e it copies inner lists as well which results in two separate lists that doesn't affect each other

