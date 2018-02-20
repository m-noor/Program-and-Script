#2520 is the smallest number that can be divided by each of the numbers from 1
#to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all of the
#numbers from 1 to 20?

i = 2

list_of_int = range(2,21) # we want the number to be divisible by each of 2-20
smallest_number = 2 #232792560 for 1-20; 2520 for 1-10; the loop can be made faster by declaring it as 2520

found_smallest_number = False

while found_smallest_number == False:
    
    while i < list_of_int[-1]:
        if (smallest_number) % i == 0:
            found_smallest_number = True
            i+=1
        else:
            i = 2
            smallest_number+=1
            found_smallest_number = False

print("Smallest number = ", smallest_number)
