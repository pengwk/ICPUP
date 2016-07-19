#!/usr/bin/env

# 5 4 3 2
# 4 3 2
# 3 2
# 2

# ans 10times wrong ans


def fib(n):
    """Assumes n an int >= 0
Returns Fibonacci of n"""
    if n == 2:
        print 2
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
fib(5)

# right is 3 times
# 5 -> 4, 3
# 
# 4 -> 3, 2
# 3 -> 2, 1
# 
# 3 -> 2, 1
# 2 -> 1, 0
# 2 -> 1, 0
# 
# 2 -> 1, 0