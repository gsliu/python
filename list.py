#!/usr/bin/python

list1 = [1, 2, 3, 4]

list2 = [2, "bbb", 88, "ccc"]

list3 = list1 +list2

print(list(list3))

list3.extend(["aaa", "ddd"])

print(list(list3))

str1 = "Hello world python"

j = len(str1) - 1

i = 0

while i <= j :
    if (str1[i] == " ") :
        i = i+1
        continue
#    print ("%d character is %s", % (i, str1[i:]))
    print ("%d character is %s" % (i, str1[i]))
    i = i +1




