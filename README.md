# Course: 52167 Programming and Scripting

This repository contains the codes for the module exercises.

### Exercises 1 and 2: Fibonacci sequence - [Fibonacci_sequence.py](Fibonacci_sequence.py)

### Exercise 3: Collatz conjecture exercise - [Collatz_conjecture.py](Collatz_conjecture.py)

### Exercise 4: Project Euler - Problem 5 

> _2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder. What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20._

For this, there are two similar but slightly different solutions:

#### [project_Euler_problem_5_whileloop.py](project_Euler_problem_5_whileloop.py) - uses only `while` loops
#### [project_Euler_problem_5_forloop.py](project_Euler_problem_5_forloop.py) - uses a mixture of `for` and `while` loops

Benchmarking with a simple `time.time()` function indicates that the the first solution with `while` loop exclusively is slightly faster: 140 vs. 174. As inspired by http://www.mathblog.dk/project-euler-problem-5/, pre-determining the prime numbers in the integer interval results in a faster performance - 0.0936 to find the smallest number divisible by integers 1-20.

Additionally, the project_Euler_problem_5_forloop.py has been modified to accept user inputs and perform automatic optimizations to arrive at the solution significantly faster.
