#!/usr/bin/python
# -*- coding: utf-8 -*-
import time,functools
def metric(fn):
    def wrapper(*args,**kw):
        time_start=time.time()
        fn(*args,**kw)
        time_end=time.time()
        print('time=',time_end-time_start,fn.__name__)
        return fn(*args,**kw)
    return wrapper
@metric
def fast(x,y):
    time.sleep(1)
    return x+y
print(fast(2,2))



def log0(fun):
    def wrapper(*args,**kw):
        print('call',fun.__name__)
        return fun(*args,**kw)
    return wrapper
@log0
def now():
    print('20190101')
now()

import functools
int2 = functools.partial(int,base=2)
print(int2('111000',base=10))

print(int('1100',8))
