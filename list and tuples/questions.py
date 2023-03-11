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

#5. what does spam[:2] evaluate to?
# displays items of list from 0 to 2

#let's pretend bacon has the list [3.14, 'cat', 11, 'cat', True] for the next three questions, 

#6 what does bacon.index('cat') evaluate to?
#index of cat i.e 1

#7. what does bacon.append(99) make the list value in bacon look like?
# adds 99 to the end of the list

#8. what does bacon.remove('cat') make the list value in bacon look like?
