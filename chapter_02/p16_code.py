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
    >>> largest_odd(17, 8, 16)
    17
    >>> largest_odd(13, 13, 12)
    13
    >>> largest_odd(13, 12, 12)
    13
    """
    _big, _mid, _small = x, y, z

    if _big % 2 != 0 or _mid % 2 != 0 or _small % 2 != 0:
        if _big < _mid:
            _big, _mid = _mid, _big

        if _big < _small:
            _big, _small = _small, _big

        if _mid < _small:
            _mid, _small = _small, _mid

        if _big % 2 == 1:
            print _big
        elif _mid % 2 == 1:
            print _mid
        elif _small % 2 == 1:
            print _small
    else:
        print "No odd!"

    return None
