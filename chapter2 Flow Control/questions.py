#1. What are the two values of the Boolean data type? How do you write them?
#True and False are the two Boolean values. They are written with the first letter capitalized.

#2. What are the three Boolean operators?
#The three Boolean operators are and, or, and not.

#3. Write out the truth tables of each Boolean operator (that is, every possible combination of Boolean values for the operator and what they evaluate to).
#True and True is True
#True and False is False
#False and True is False
#False and False is False

#True or True is True
#True or False is True
#False or True is True
#False or False is False

#not True is False
#not False is True

#4. What do the following expressions evaluate to?
# (5 > 4) and (3 == 5)   is False
# not (5 > 4)        is False
# (5 > 4) or (3 == 5)  is True
# not ((5 > 4) or (3 == 5))  is False 
# (True and True) and (True == False)  is False
# (not False) or (not True)  is True

#5. What are the six comparison operators?
#The six comparison operators are <, >, ==, >=, <=, and !=.

#6. What is the difference between the equal to operator and the assignment operator?
#The equal to operator (==) asks if two values are the same as each other. The assignment operator (=) puts the value on the right into the variable on the left.


#7. Explain what a condition is and where you would use one.
#A condition is an expression used in a flow control statement that evaluates to True or False. You would use a condition in an if statement to determine which block of code to execute.


#8. Identify the three blocks in this code:
# spam = 0
# if spam == 10:
#     print('eggs')
#     if spam > 5:
#         print('bacon')
#     else:
#         print('ham')
#     print('spam')
# print('spam')

#The three blocks are the if block, the else block, and the print('spam') line.


#9. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.
spam = int(input("enter a number: "))
if spam == 1:
    print("Hello")
elif spam == 2:
    print("Howdy")
else:
    print("Greetings!")
    
    
    
#10. What keys can you press if your program is stuck in an infinite loop?
# ctrl + C

#11. What is the difference between break and continue?
#The break statement will move the execution outside and just after a loop. The continue statement will move the execution to the start of the loop.


#12. What is the difference between range(10), range(0, 10), and range(0, 10, 1) in a for loop?
print(range(10))
print(range(0, 10))
print(range(0, 10, 1))

#The range(10) call ranges from 0 to 9 (10 numbers). The range(0, 10) call also ranges from 0 to 9 (10 numbers). The range(0, 10, 1) call also ranges from 0 to 9 (10 numbers). All three of these calls would result in the same printed output.

#13. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.
for i in range(1, 11):
    print(i)

i = 1
while i < 11:
    print(i)
    i += 1
    
    
#14. If you had a function named bacon() inside a module named spam, how would you call it after importing spam?
#import spam
#spam.bacon()