# -*- coding: utf-8 -*-
__author__ = 'Vietworm'
import Problem1
import Problem2

"""Problem 1:
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""

if Problem1.sumMultiples() == 233168:
    print "Problem 1 solved!"

"""Problem 2:
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""

if Problem2.sumFibonacci(4000000) == 4613732:
    print "Problem 2 solved!"