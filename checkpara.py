#!/usr/bin/python

def check ( para={"aaa":1, "ccc":2}):
    if type(para) == type( {}):
        print "dict"
    elif type(para) == type ([]):
        print "list"
    elif type(para) == type (""):
        print "string"
    else:
        print "I don't know this type"



a = {"aaa":1, "bbb":2}
b = [1,2,3]
c = "jjjj"

check(a)
check(b)
check(c)
check()
