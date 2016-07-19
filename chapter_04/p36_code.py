#!/usr/bin/env 

def isIn(str_one, str_two):
    if str_one in str_two or str_two in str_one:
        return True
    else:
        return False

## version2
def isIn(str_one, str_two):
    return str_one in str_two or str_two in str_one