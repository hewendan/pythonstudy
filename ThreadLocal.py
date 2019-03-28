#!/usr/bin/python
# -*- coding: utf-8 -*-
import threading
local_school=threading.local()
def process_student():
    std = local_school.student
    print('Hello,%s in %s' % (std,threading.current_thread().name))
def process_thread(name):
    local_school.student = name
    process_student()
t1=threading.Thread(target=process_thread, args=('AA',), name='Thread-A')
local_school.student = 'CC'
t1.start()
t1.join()
std = local_school.student
print('Hello,%s in %s' % (std,threading.current_thread().name))
t2=threading.Thread(target=process_thread, args=('BB',), name='Thread-B')
t2.start()
t2.join()
