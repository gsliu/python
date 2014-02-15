#!/usr/bin/python

f = open("testfile", "rw")
#print f

#c = f.read()

#print c

#d = f.readline()
#print d

#f = f.readline()

#print f
#i = 1
#for line in f:
 #   print("line %d : %s" % (i, line))
#    i = i + 1

#f.write("this a test file")

def printalllines(fi) :
    print list(fi.readlines())


printalllines(f)
