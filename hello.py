#!/usr/bin/python
# -*- coding: utf-8 -*-
print('helloworld')
print(100+200+300)
x=int(input('x='))
y=input()
print('x*y=',int(x)*int(y))
if x>=0:
    print(x)
else:
    print(-x)
print('\n\nhehe')
print(r'\n\nhehe')
str=b'ABC'.decode('ascii') #要把bytes变为str，就需要用decode()方法
str1='ABC'.encode('ascii') #以Unicode表示的str通过encode()方法可以编码为指定的bytes
print(str1)
print(str)
s1=72
s2=85
r=(s2-s1)/s1*100
print('%.1f\n'% r)
def my_abs(x):
    if x>=0:
        print (x)
    else:
        print (-x)


my_abs(-5)
def calc(*numbers):
    sum=0
    for n in numbers:
        sum = sum + n*n
    return sum
print(calc(1,2,3))
nums=[1,2,3]
print(calc(*nums))#*nums表示把nums这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见。

def trim(s): #去除字符串首尾的空格
    while(s[:1]==' '):
        s=s[1:]
    while(s[-1:]==' '):
        s=s[:-1]
    return s
print(trim('   he   he  www  '))


def findMinandMax(L):
    if len(L)==0:
        return None,None
    if len(L)==1:
        return L[0],L[0]
    L.sort()
    return L[0],L[-1]

print(findMinandMax([2]))
print(findMinandMax([2,2,3,4,5,7,8,4]))

