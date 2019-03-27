#!/usr/bin/python
# -*- coding: utf-8 -*-
L=[('A',1),('B',2),('D',4),('C',3)]
def kk(T):
    return T[0]
print(sorted(L,key=kk))
def count():
    fs=[]
    for i in range(1, 4):
        def f():
            return i*i
        print('i=',i)
        fs.append(f)
    return fs
f1,f2,f3=count()
print(f1())
def createCounter():
    nn=0
    def tt():
        nonlocal nn
        nn=nn+1
        return nn
    return tt
createA=createCounter();
print(createA())
print(createA())
print(createA())
print(createA())
def build(x,y,z=0):
    return lambda :x*x+y*y
print(build(2,3)())


L = list(filter(lambda x:x%2==1, range(1, 20)))
print(L)
