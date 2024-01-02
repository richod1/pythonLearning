#python list
myname=["degraft","frimpong","kweku"]
print(myname)
#length of list
print(len(myname))

if "kwesi" in myname:
    print("yes degraft exist in myname")
else:
    print("name dont exist")

myname.append("silverdollor")
print(myname)

myname.insert(2,"kwekudolor")
print(myname)

mycar=["benz","toyota","suzuki"]

myname.extend(mycar)
print(myname)

print(">>>>>>>>>>>")
mycar.remove("suzuki")
print(mycar)

mycar.pop(0)
print(mycar)

thelist=["apple","banana","mango"]
for i in range(len(thelist)):
    print(thelist[i])

    #using the while loop
    print("<<<<<<<<<<<<<<<")
count=0
while count< len(thelist):
    print(thelist[count])
    count=count+1

    print("<<<<<<<<")

my_fruit=["banan","cherry","coconut","cocoa"]
newfruit=[]

for x in my_fruit:
    if "a" in x:
        newfruit.append(x)
print(newfruit)

print("<<<<<<<<")
myNum=[x for x in range(10) if x < 5]
print(myNum)

unsorted_numbers=[10,9,7,5,4,3,2,1,2,4,5,6,8,9]
remove_duplicate=list(set(unsorted_numbers))
print(remove_duplicate)


print("<<<<<<<<<<<")
this_list=["orange","mango","pinapple","banana"]
this_list.sort()
print(this_list)

#reverse sort
this_list.sort(reverse=True)
print(this_list)





