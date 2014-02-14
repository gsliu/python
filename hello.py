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
#print ("filler = %s" % filler)

a = ("first", "second", "third")
b = (a, "b's second element")
print ( "%s" % a[1])
print ( "%s" % b[0][1])

print ( "%s" % b[1][0])
print ( "%s" % b[1][1])
print ( "%s" % b[1][3])

array = [ "coffee", "tea", "toast" ]

print array[2]

array.append("aaa")

print array[3]

memu = {}

memu["breakfast"] = "china"
memu["lunch"] = "tuna"

print memu["breakfast"]

print(list(memu.keys()))

print list([ "aaa","bbb" ])


print len(["aaa","bbb"])


array.append(array)

print array


array.append(list(array))

print array


print len(array)

print array[2:4]

print slice(array)


