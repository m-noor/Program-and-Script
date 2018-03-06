# Please complete the following exercise this week.  Write a Python script containing a function called factorial() that takes a single input/argument which is a positive integer and returns its factorial.  The factorial of a number is that number multiplied by all of the positive numbers less than it.
# For example, the factorial of 5 is 5x4x3x2x1 which equals 120.  You should, in your script, test the function by calling it with the values 5, 7, and 10.

import math
is_integer = False

def factorial(integer):
    
    result = math.factorial(integer)
    print('The factorial of', integer, 'is:', result)

# for testing the function
factorial(5)
factorial(7)
factorial(10)

# request user's input and check it is a positive integer
while is_integer == False:
    
    integer = input('Enter a positive integer: ')
    
    try:
        if (integer.isnumeric() == True) and (int(integer) > 0):
            integer = int(integer)
            is_integer = True
    except ValueError: 
        pass

# run the function to calculate factorial
factorial(integer)
