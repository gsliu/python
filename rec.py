#!/usr/bin/python

print __name__
print __date__
print __author__


def F(i=10):
    if i==0 :
        raise TypeError("i=0")
        return 1
    if i==1 :
        return 1
    return F(i-1) + F(i-2)


print F(20)
