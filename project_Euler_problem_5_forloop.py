found_smallest_number=False

# for a number to be divisible by all integers a to b, this number should be divisible by all the prime numbers which is equivalent to 19*17*13*11*7*5*3*2. so we should start our search from 9699690 (instead of 2) and then increment it by the same.
# inspired by: http://www.mathblog.dk/project-euler-problem-5/

smallest_number=9699690

while found_smallest_number == False:
    for i in range(2,21): # all numbers are divisible by 1, so just start from 2
        #print(i)
        if smallest_number % i == 0:
            found_smallest_number = True
        else:
            smallest_number+=9699690            
            found_smallest_number = False
            break # exit the inner for loop and restart all over with new number

print("Smallest number: ", smallest_number) #232792560 for 1-20; 2520 for 1-10; the loop can be made slightly faster by setting smallest_number to 2520
