#!/usr/bin/python
# -*- coding: utf-8 -*-
name=input('请输入的你姓名:')
height=float(input('请输入你的身高:'))
weight=float(input('请输入你的体重:'))
BMI=float('%.2f'%(weight/pow(height,2)))
if BMI<18.5:
    print('\n%s的BMI为'%(name),BMI,'过轻\n')
elif BMI<25:
    print('\n%s的BMI为'%(name),BMI,'正常\n')
elif BMI<28:
    print('\n%s的BMI为'%(name),BMI,'过重\n')
elif BMI<32:
    print('\n%s的BMI为'%(name),BMI,'肥胖\n')
else:
    print('\n%s的BMI为'%(name),BMI,'严重肥胖\n')
