found_smallest_number=False

# for a number to be divisible by all integers a to b, 
# instead of 2 # this number should be divisible by all the prime numbers which is equivalent to 19*17*13*11*7*5*3*2
# inspired by: http://www.mathblog.dk/project-euler-problem-5/

smallest_number=9699690

while found_smallest_number == False:
    for i in range(2,21): # all numbers are divisible by 1, so just start from 2
        #print(i)
        if smallest_number % i == 0:
            found_smallest_number = True
            # i+=1
        else:
        #    i=2
            smallest_number+=9699690
            #if smallest_number == 232792560:
            print(smallest_number)
            found_smallest_number = False
            break # exit the inner for loop and restart all over with new number

print("Smallest number = ", smallest_number) #232792560 for 1-20; 2520 for 1-10; the loop can be made slightly faster by setting smallest_number to 2520

