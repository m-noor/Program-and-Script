
def fib(n):
  """This function returns the nth Fibonacci number."""
  i = 0
  j = 1
  n = n - 1

  while n >= 0:
    i, j = j, i + j
    n = n - 1
  
  return i

name = "Noor"
first = name[0]
last = name[-1]
firstno = ord(first)
lastno = ord(last)
x = firstno + lastno

ans = fib(x)
print("My surname is", name)
print("The first letter", first, "is number", firstno)
print("The last letter", last, "is number", lastno)
print("Fibonacci number", x, "is", ans)
print('\n' + '\n'  + "What does ord() function do?" + '\n')
print(help(ord))

# Week 1 output
# My name is Mohamed, so the first and last letter of my name (M + D = 13 + 4) give the number 17. The 17th Fibonacci number is 1597.


# Week 2 output
#My surname is Noor.

#The first letter N is number 78
#The last letter r is number 114
#Fibonacci number 192 is 5972304273877744135569338397692020533504

#ord(c, /)
#    Return the Unicode code point for a one-character string.
