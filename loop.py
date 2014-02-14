#!/usr/bin/python

f = {"egg" : 1, "cheese" : 2, "san" :3 }

for i in list(f.keys()) :
    print f[i]


try:
    if f["jjjj"] == 3 :
        print "f[jjjj] found"
except KeyError:
    print "Awww. failed in key"
