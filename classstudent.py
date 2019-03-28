#!/usr/bin/python
# -*- coding: utf-8 -*-
class Student(object):
    def __init__(self,name,gender):
        self.name = name
        self.__gender = gender
    def set_gender(self,gender):
        self.__gender = gender
    def get_name(self):
        return self.name
    def get_gender(self):
        return self.__gender
class SS(object):
    def get_name(self):
        return 'hh'

def getget(object):
    return object.get_name()
bart=Student('hewd',99)
ss = SS()
print(getget(bart),getget(ss))
print(ss.get_name())
print(bart.get_name())
print(bart.get_gender())
print(bart.name,bart._Student__gender)
print(dir(bart))
class TT(object):
    __slots__=('name','age')
t=TT()

class Screen(object):
    w=0
    h=0
    @property
    def resolution(self):
        self._resolution=self.w*self.h
        return self._resolution

screen=Screen()
print(screen.resolution)
screen.w=10
screen.h=10
print(screen.resolution)
print(screen.__dict__)
