"""from math import sqrt
from copy import copy

class Point:
    def __init__(self,x=0.0,y=0.0):
        self.x=x
        self.y=y
    def __repr__(self):
        return "({},{})".format(self.x,self.y)
    def distance_from_origin(self):
        return sqrt(self.x*self.x+self.y*self.y)
    def translate(self,shift_x,shift_y):
        self.x+=shift_x
        self.y+=shift_y
    def opposite(self):
        self.x=-self.x
        self.y=-self.y

#Create a list of all the points with integer coordinates, with both their x and y coordinates ranging from 0 to 3.
pointList=[]
for i in range(3):
    for j in range(3):
        pointList.append(Point(i,j))
print(pointList)



class Rectangle:
    def __init__(self, point, width, height):
        self.point=copy(point)
        self.width=abs(width)
        self.height=abs(height)
    def __repr__(self):
        return "[{},w = {},h = {}]".format(self.point,self.width,self.height)
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2*self.width + 2*self.height
    def BRcorner(self):
        return Point(self.point.x + self.width, self.point.y + self.height)



r1=Rectangle(Point(3,4),2,5)
BR=r1.BRcorner()
r2=Rectangle(Point(2,6),4,4)"""


#A student has a last name, a first name, a date of birth (either a year, month, and day,
# or a datetime object if you took the liberty of studying the datetime module already),
# and an administration number. A course has a name and a number. Students can enroll in courses.
# Create a class Student and a class Course. Create several students and several courses.
# Enroll each student in some of the courses. Display a list of students, showing their number,
# first name, last name, and age, and per student which courses he or she is enrolled in.

class Student:
    def __init__(self,surname,name,day,month,year,adminN):
        self.surname=surname
        self.name = name
        self.day = day
        self.month = month
        self.year = year
        self.adminN = adminN
        self.courses = []
    def __repr__(self):
        print ("{} {}, DoB: {}/{}/{}, ID = {}".format(self.surname, self.name, self.day,
                                                        self.month, self.year, self.adminN))
    def enroll(self,course):
        if course not in self.courses:
            self.courses.append(course.name)
    def age(self,today,thismonth,thisyear):
        if (thismonth < self.month) or (thismonth == self.month and today < self.day):
            return thisyear - self.year -1
        else:
            return thisyear - self.year



class Course:
    def __init__(self,cname,cnumber):
        self.cname = cname
        self.cnumber = cnumber
    def __repr__(self):
        print("Course: {}, Course Number: {}".format(self.cname,self.cnumber))



s1=Student("Mario", "Rossi",25,11,1991,276545)
s2=Student("Anna", "Verdi", 23, 4, 1992, 485745)
s3=Student("Fabio", "Neri", 12,2,1992, 200768)
c1=Course("AllPy",101,[])
c2=Course("AllDB",104,[])









