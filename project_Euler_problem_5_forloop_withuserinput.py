# 2520 is the smallest number that can be divided by each of the numbers from 1
# to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the
#numbers from 1 to 20?

# To answer this, we use a bit of a priori math knowledge, instead of a brute-force search. Inspired by: http://www.mathblog.dk/project-euler-problem-5/

# First, we know for this smallest number must be divisible by all the prime numbers in that range.

# Second, we test increments of the product of these prime numbers.

# As a further extension of the problem, we also allow the user to input any integer > 1 (n) to search for a smallest number divisible by integers 1 to n.

def primeSieve(sieveSize):
    # Wikipedia: Sieve of Eratosthenes is a simple, ancient algorithm for finding all prime numbers up to any given limit. See the pseudocode in the entry.
    # The code below is modified/tidied up from: https://inventwithpython.com/hacking/chapter23.html. Additionally, we don't need to import math module - sqrt(n) is equivalent to pow(n,0.5)

    # 1. create a list holding a Boolean of 'is prime/is not prime' for each number
    sieve = [True] * sieveSize
    sieve[0], sieve[1] = False, False # 0 and 1 are not prime numbers

    # 2. create the sieve, with an optimization step where we know the multiples of each prime i to i^2 are not prime numbers
    for i in range(2, int(pow(sieveSize, 0.5)) + 1):
       pointer = i * 2
       while pointer < sieveSize:
           sieve[pointer] = False
           pointer += i

    # 3. collect all the 'True' entries (prime numbers)

    primes = [] # empty list to hold our prime numbers

    for i in range(sieveSize):
        if sieve[i] == True:
            primes.append(i)

    #4. for our purpose, to optimize the search for the actual smallest number, we need to find the product of all the prime numbers in the primeSieve and search in increments of this product.
    
    increment = 1
    for i in range(len(primes)):
        increment = increment * primes[i]

    return increment

# re-use the code from Collatz_conjecture - loop until the user enters a positive integer

is_integer = False
while is_integer == False:
    sieveSize = input("Enter the higher end of the range for which you would like to find the smallest positive integer divisible by all the numbers in the range: ")
    
    try:
        if (sieveSize.isnumeric() == True) and (int(sieveSize) > 0):
            sieveSize = int(sieveSize)
            is_integer = True
    except ValueError:
        pass
    
increment = primeSieve(sieveSize)
smallest_number=increment # start searching with the product of prime numbers

found_smallest_number = False

while found_smallest_number == False:
    for i in range(2, sieveSize + 1): # all numbers are divisible by 1, so just start from 2        
        if smallest_number % i == 0:
            found_smallest_number = True
        else:
            smallest_number = smallest_number + increment
            found_smallest_number = False
            break # exit the inner for loop and restart all over with new number

print("Smallest number: ", smallest_number) #232792560 for 1-20; 2520 for 1-10
