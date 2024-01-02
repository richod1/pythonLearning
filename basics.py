#using the sort method in list
thislist=["orange","mango","kiwi","banana"]
thislist.sort()
print(thislist)

#to reverse sorted list
thislist.sort(reverse=True)
print(thislist)

#sort customization
def myFunc(n):
    return (n-50)

the_list=[100,60,65,82,23]
the_list.sort(key=myFunc)
print(the_list)

#list copy()


print("<<<<<<<<<<")
mylist=thislist.copy()
print(mylist)

#joining two list
for x in the_list:
    thislist.append(x)

print(thislist)

#using the extend method
print("<<<<<<<<")
thislist.extend(the_list)
print(thislist)


#python tuples
this_tuple=("apple","mango","banana")
print(len(this_tuple))

for i in this_tuple:
    print(i)

single_tuple=("mango")
print(type(single_tuple))

print(type(this_tuple))

#set
this_set={"apple","cherry","mango","apple"}
print(this_set)

for a in this_set:
    print(a)
    if "mango" in this_set:
        print("mango is available in the set")


tropical={"pinapple","coconut","mango"}
#adding two set together by using the update method
this_set.update(tropical)
print(this_set)

#python dictionary
#python dictionary is similar to js object but not orderd and also accept multiple data types
school_items={
    "laptop_name":"Hp",
    "bag_name":"gucci",
    "water_bottle":"can pipe"
}
print(school_items["bag_name"])

#conditional statement in python
a=200
b=500
if a < b:
    print("a is lesser")
else:
    print("b is greater")

#fizz buzz in  python

def fizzBuzz(n):
    for i in range(1,n+1):
        if i%3 ==0 and i%5==0:
            print("FizzBuzz")
        elif i%3==0:
            print("Fizz")
        elif i%5 ==0:
            print("Buzz")
        else:
            print(i)

fizzBuzz(15)

#while loop
number=1
while number<20:
    print(number)
    number+=1

numbers=1
while numbers < 6:
    print(numbers)
    if numbers ==3:
        break
    numbers +=1

#while continue statements
num1=0
while num1 <7:
    num1 +=1
    if num1==4:
        continue
    print(num1)

#for loop in python
friut=["pine","cherry","lemon","orange"]
for x in friut:
    print(x)
    if x == "cherry":
        break

print("<<<<<")
#continue statement in loop
for x in friut:
    if x == "lemon":
        continue
    print(x)


#range in loop
for x in range(2,6):
    print(x)


adj = ["red", "big", "tasty"]
fruitts = ["apple", "banana", "cherry"]

for x in adj:
    for j in fruitts:
        print(x,j)