# _*_ coding:utf-8 _*_

def sumDigits(s):
    """Assumes s is a string
       Return the sum of the decimal digits in s
       For example, if s is 'a2b3c' it returns 5"""
    _sum = 0
    for char in s:
        try:
            _sum += int(char)
        except:
            pass
    return _sum

if __name__ == '__main__':
    print sumDigits("a2b3x")