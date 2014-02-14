#!/usr/bin/python

data1 = [1, 2, 3, 4, 5]
print data1.pop(3)

print data1


data2 = [ 'a', 'b', 'c', 'a', 'b' ]
data2 = set(data2)

print(list(data2))

i=1
j=20
str1="aaa"
str2="bbb"
str3="ccc"
str4="aaa"

if i==j:
    print "i==j"
else :
    print "j!=j"

if not str1==str4:
    print("not str1==str4")
    print("ggggg")
print("hereaaa")


while  i < j :
    print i
    i = i+1
print "end of loop"

for c in data2 :
    print c
else :
    print "end of c"
