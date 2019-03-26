#!/usr/bin/python
# -*- coding: utf-8 -*-
from functools import reduce
def triangles(max):
    n,a,b =0,0,1
    L=[]
    while n <max:
        L.append(b)
        yield b
        a,b = b,a+b
        n=n+1
    return L
#print(triangles(10))
def triangles():
    L=[1]
    while 1:
        yield L
        L=[1]+[L[i]+L[i+1] for i in range(len(L)-1)]+[1]
        print(L)
n=0;
for t in triangles():
    print(t)
    n=n+1
    if(n>1):#n>10
        break
def add(x,y,f):
    return f(x)+f(y)
f=abs
print(add(-2,-2,f))
def str2float(s):
    i = s.find('.')
    print(i)
    if i:
        i=s.index('.')
    def fn(L):
        return reduce(lambda x,y:x*10+y,map(int,L))
    print(fn(s[:i]))
    print(fn(s[i+1:]))
    return fn(s[:i])+fn(s[i+1:])/10**len(s[i+1:])
print(str2float('11223.223235'))

def is_palindrome(n):
    t=str(n)
    a=0
    for i in range(len(t)):
        if(t[i]==t[-1-i]):
            a=a+1
    return a==len(t)

output = filter(is_palindrome, range(1, 100))
print(list(output)) 
output = filter(is_palindrome, range(1, 100))
LL=list(output)
print(LL)
