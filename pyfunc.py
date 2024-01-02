import pymodule
import platform
import datetime
import json
import math
import  camelcase
import os
def fullName(fname):
    print(fname + " Frimpong")


fullName("Degraft")

def my_function(*names):
    print("my names are " + names[3])

my_function("Degraft ","Frimpong","Kweku","Dollor")

def array_func():
    cars=["toyota","Benz","Camery"]
    cars.append("Honda")
    print(cars)

array_func()


#python class
class Person:
    def __init__(self,name,age,work):
        self.name=name
        self.age=age
        self.work=work

P1=Person("Dagreft",23,'Software engineer')

print(P1.name)
print(P1.work)

#python inheritence


class Parent:
    def __init__(self,firstname,lastname):
        self.firstname=firstname
        self.lastname=lastname

    def printname(self):
        print(self.firstname,self.lastname)

parent_name=Parent("Degraft","Frimpong")
parent_name.printname()

class Student(Parent):
    pass

person_student=Student("Kweku","Frimpong")
person_student.printname()

#using the iter method
myTuple=("apple","banana","cherry")
myit=iter(myTuple)

print(next(myit))

pymodule.greeting("Frimpong")

user_computer=platform.system()
print(user_computer)

tody_date=datetime.datetime.now()
print(tody_date)

#user input date
usr_date=datetime.datetime(2023,12,5)
print(usr_date.strftime("%C"))

#python math method
square_of_root=math.sqrt(20)
print(math.floor(square_of_root))

cities='{ "name":"John", "age":30, "city":"New York"}'
western_cities=json.loads(cities)

print(western_cities["name"],"\n",western_cities["age"])


c=camelcase.CamelCase()
FullName="degraft frimpong"
print(c.hump(FullName))


my_File=open("demo.txt","r")
print(my_File.read())
for x in my_File:
    print(x)

my_second_file=open("demo2.txt","a")
my_second_file.write("Am here to code and code only")
my_second_file.close()


#read file
my_second_file=open("demo2.txt","r")
print(my_second_file.read())

#remove file
if os.path.exists("demo.txt"):
    os.remove()
else:
    print("file dont exist")
