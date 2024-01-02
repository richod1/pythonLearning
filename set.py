
import pymodule

fruit={"apple","pawpaw","mango"}
print(fruit)

# to add to set
fruit.add("cashew")
print(fruit)
fruit_drink={"don simon","apple_juice","lemonade"}
# adding two set using the update()

fruit.update(fruit_drink)
print(fruit)


fruit.remove("apple")
print(fruit)

# loop in set
for n in fruit:
    print(n)

name="degraft frimpong"

while name == "degraft frimpong":
    print("name is ", name)
    if name=="degraft frimpong":
        break




i=20
while i < 6:
    print(i)
    if i==2:
        break
    i +=1

vegetable=["carrot","beans","cabbage"]

for n in vegetable:
    if n == "beans":
        break
    print(n)
numbers=[1,2,3,4,5,6]
for index,value in enumerate(range(4)):
    if index == 3:
        print(f"Index of :{value} is {index}")


def my_function(*kids):
    print("the youngest child is " ,kids[2])


my_function("degraft","frimpong","kweku")

def the_function(**kid):
    print("His last name is " + kid["lname"])

the_function(fname="degraft",lname="frimpong")

# lamda function
add_lambda=lambda x,y:x+y
result=add_lambda(3,5)
print(result)


my_numbers=[1,2,3,4,5]
sqaured=map(lambda x:x**2,my_numbers)
print(list(sqaured))

# class in python
class Person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname

    def __str__(self):
        return f"my name is {self.fname} {self.lname}"


person=Person("degraft","frimpong")
print(person)

mygreet=pymodule.greeting("good morning")
print(mygreet)