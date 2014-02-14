#!/usr/bin/python
import sys
print("hello world" )
print("test %s, %s" % ("hahha", "gagaga"))
i=12
print(" %d, %s" %(i,type(12)))

print("sys.path = %s " % (sys.path))

a = " string a"
b = " string b"
c = a + b;
print(c)

filler = ("abc", "def", "jjj%s" % (a), "ffff")
print filler
print ("filler = %s" % filler)
