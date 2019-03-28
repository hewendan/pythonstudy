#!/usr/bin/python
# -*- coding: utf-8 -*-
def fact(n):
    '''
    Calculate 1*2*...*n

    >>> fact(1)
    1
    >>> fact(10)
    362880
    >>> fact(2)
    2
    '''
    if n < 1:
        raise ValueError()
    if n == 1:
        return 1
    return n * fact(n - 1)
if __name__ =='__main__':
    import doctest
    doctest.testmod()
