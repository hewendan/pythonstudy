#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
class student(object):
    name='he'
    age=18
s=student()
s.name='wen'
s.age=18
print(s.age)
print(s.__dict__)
print(json.dumps(s,default=lambda obj:obj.__dict__))

oo = dict(name='xiaoming小明',age=20)
s = json.dumps(oo,ensure_ascii=False)
print(s)
s = json.dumps(oo)
print(s)
