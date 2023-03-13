# 1. Why are functions advantageous to have in your programs?
# Function are needed to make programs more readable and manageable. It's also easier to debug a program if it's broken down into functions. We also don't need to write same code multiple times instead it's lot easier to use a function.

# 2. When does the code in a function execute: when the function is defined or when the function is called?
# The code in a function executes when the function is called.


# 3. What statement creates a function?
# def statement creates a function.


# 4. What is the difference between a function and a function call?
# A function is a block of code that is defined for a specific task. A function call is the code that is used to execute the function.


# 5. How many global scopes are there in a Python program? How many local scopes?
# There is only one global scope, and a local scope is created whenever a function is called.



# 6. What happens to variables in a local scope when the function call returns?
# The space allocated for the variable is released when the function call returns. The variable is destroyed.



# 7. What is a return value? Can a return value be part of an expression?
# A return value is the value that a function call evaluates to. Like any value, a return value can be used as part of an expression.



# 8. If a function does not have a return statement, what is the return value of a call to that function?
# If there is no return statement for a function, its return value is None.


# 9. How can you force a variable in a function to refer to the global variable?
# By using the global statement.



# 10. What is the data type of None?
# The data type of None is NoneType.


# 11. What does the import areallyourpetsnamederic statement do?
# This import statement imports a module named areallyourpetsnamederic. If the import statement fails, which it most likely will, because there is no such module named areallyourpetsnamederic, then a Traceback error message will be displayed.


# 12. If you had a function named bacon() in a module named spam, how would you call it after importing spam?
# bacon.spam()

# 13. How can you prevent a program from crashing when it gets an error?
# by using try and except statements.



# 14. What goes in the try clause? What goes in the except clause?\
# The code that could potentially cause an error goes in the try clause. The code that executes if an error happens goes in the except clause.