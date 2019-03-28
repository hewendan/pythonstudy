#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
print('Proces (%s) start....' % os.getpid())
pid=os.fork()
if pid==0:
    print(os.getpid())
else:
    print(os.getpid())
