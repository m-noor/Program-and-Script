# The Collatz conjecture program by Mohamed Noor
# If the number is even, divide it by two.  n/2
# If the number is odd, triple it and add one.  3n+1

# 1.  first, check to ensure n is a positive integer
n = None # declare an empty variable
is_integer = False

# loop until the user enters a positive integer for the while loop below
while is_integer == False:
    
    n = input("Enter a positive integer: ")

    try:
        if (n.isnumeric() == True) and (int(n) > 0):
            n = int(n)
            print(n)
            is_integer = True
    except ValueError: 
        pass # do nothing - in Python, can't have empty line

# 2.  second, check if n is even or odd.  no need to convert into an int anymore. And, loop the whole thing.

while n > 1:
    if n % 2 == 0: # even
        n = n // 2 # in Python 3, int divided by integer is a float (10/2=5.0) . so we do floor division instead
    else: # no further checks needed as we've taken care of it above
        n = 3 * n + 1

    print(n)


#Please complete the following exercise this week. In the video lectures we discussed the Collatz conjecture. Complete the exercise discussed in the Collatz conjecture video by writing a single Python script that starts with an integer and repeatedly applies the Collatz function (divide by 2 if even, multiply by three and 1 if odd) using a while loop and if statement. At each iteration, the current value of the integer should be printed to the screen. You can specify in your code the starting value of 17. If you wish to enhance your program, have the program ask the user for the integer instead of specifying a value at the start of your code. Add the script to your GitHub repository, as per the instruction in the Assessments section.
