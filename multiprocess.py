#!/usr/bin/python
# -*- coding: utf-8 -*-
from multiprocessing import Process,Queue
import os,time,random,multiprocessing
def write(q):
    print('Process write %s' % os.getpid())
    for value in ['a','b','c']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())
def read(q):
    print('Process read %s' % os.getpid())
    while True:
        print('start get q')
        value=q.get(True)
        print('get %s to queue...' % value)
if __name__=='__main__':
    q=Queue()
    pw=Process(target=write,args=(q,))
    pr=Process(target=read,args=(q,))
    pw.start()
    pr.start()
    pw.join()#等待结束
    pr.terminate()#强制退出
    print(multiprocessing.cpu_count())
