# Course: 52167 Programming and Scripting

This repository contains the codes for the module exercises. The README was formatted according to [GitHub Help](https://help.github.com/articles/basic-writing-and-formatting-syntax/).

### Exercises 1 and 2: Fibonacci sequence - [Fibonacci_sequence.py](Fibonacci_sequence.py)

This script returns the nth Fibonacci number as a function of input string Unicode values.

### Exercise 3: Collatz conjecture exercise - [Collatz_conjecture.py](Collatz_conjecture.py)

From Wikipedia: The Collatz conjecture is a conjecture that concerns a sequence defined as follows: start with any positive integer n. Then each term is obtained from the previous term as follows: if the previous term is even, the next term is one half the previous term. Otherwise, the next term is 3 times the previous term plus 1. The conjecture is that no matter what value of n, the sequence will always reach 1. 

This script takes in an input, performs the calculation as above and return the final value. Input validation has also been built in to avoid user from entering non-integers etc.

### Exercise 4: Project Euler - Problem 5

> _2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder. What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20._

For this, there are two similar but slightly different solutions:

#### [project_Euler_problem_5_whileloop.py](project_Euler_problem_5_whileloop.py) - uses only `while` loops
#### [project_Euler_problem_5_forloop.py](project_Euler_problem_5_forloop.py) - uses a mixture of `for` and `while` loops

Benchmarking with a simple `time.time()` function indicates that the the first solution with `while` loop exclusively is slightly faster: 140 vs. 174. As inspired by http://www.mathblog.dk/project-euler-problem-5/, pre-determining the prime numbers in the integer interval results in a faster performance - 0.0936 to find the smallest number divisible by integers 1-20.

Additionally, the [project_Euler_problem_5_forloop_withuserinput.py](project_Euler_problem_5_forloop_withuserinput.py) can accept user inputs and perform automatic optimizations to arrive at the solution significantly faster.

### Exercise 5: Input and Output - [File_IO.py](FileIO.py)

This script takes as an input a user-selected csv file containing the [Iris data set](https://en.wikipedia.org/wiki/Iris_flower_data_set) and prints out the content.

### Exercise 6: Functions - [factorial_function.py](factorial_function.py)

This is a simple script to calculate the factorial of an integer using the math.factorial() function.
