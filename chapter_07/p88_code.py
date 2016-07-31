# _*_ coding:utf-8 _*_

def findAnEven(l):
    """Assumes l is a list of integers
       Return the first even number in l
       Raise ValueError if l does not contain an even number"""
    for integer in l:
        if integer % 2 == 0:
            return integer
    raise ValueError("l does not contain an even number")

if __name__ == '__main__':
    hasEven = [1, 3, 5, 4]
    noEven = [1, 3, 5]
    print findAnEven(hasEven)
    print findAnEven(noEven)