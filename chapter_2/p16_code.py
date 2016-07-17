#!/usr/bin/env 
#_*_ coding: utf-8 _*_

# 
def largest_odd(x, y, z):
    """
    >>> largest_odd(1, 3, 4)
    3
    >>> largest_odd(2, 2, 2)
    No odd!
    >>> largest_odd(3, 8, 16)
    3
    """
    if x%2 != 0 or y%2 != 0 or z%2 != 0:
        if x < y:
            x, y = y, x
        if x < z:
            x, z = z, x
        if y < z:
            y, z = z, y
        if x%2 == 1:
            print x
        elif y%2 == 1:
            print y
        elif z%2 == 1:
            print z
    else:
        print "No odd!"

    return None