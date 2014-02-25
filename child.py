#!/usr/bin/python

import os
import ctypes
import time

libc=ctypes.CDLL('libc.so.6')

for i in xrange(4):
    pid = os.fork()
    if pid == 0:
        libc.prctl(1,15)
        while True :
            print 'child ', i
            time.sleep(1)
        raise SystemExit

print 'wait for 10 second'
time.sleep(10)
print 'exit'
