#!/usr/bin/python

class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    description = "this is a shap"
    author = "nobody"
    def area(self):
        return self.x*self.y
    def perimeter(self):
        return 2*self.x+2*self.y
    def describe(self,text):
        self.description = text
    def author(self, text):
        self.author = text
    def getdescription(self):
        return self.description
    def getauthor(self):
        return self.author


re = Shape(100,100)

print re.area()

for i in re.getdescription().upper() :
    i.upper()
    print i


class Square(Shape):
    def __init__(self, x):
        self.x = x
        self.y = x


s = Square(40)

print s.perimeter()
print s.getdescription()
print s.area()


d = {}

d["retangle"] = Shape(30,40)
d["square"] = Square(50)

print d["retangle"].area()

print d["square"].area()
