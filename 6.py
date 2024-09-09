# LIST 

# Lists are used to store multiple items in a single variable.

list = ["Apple", "Banana","Lichi"]
print(list[0])
print(list[1])
print(list[2])
print(list)
print(len(list))


# LIST ITEM DATATYPES ARE
 
list1 = ["Tomato", "Potato", "Onion"]
list2 = [12 , 12.5 , 22.5]
list3 = [True , False , True]

print(list1)
print(list1[0])
print(list1[1])
print(list2)
print(list2[2])
print(list2[1])
print(list3)
print(list3[0])
print(list3[1])


names = ("AKBAR","SALEEM","JODHA","JAHANGIR")
names1 = list(("AKBAR","SALEEM","JODHA","JAHANGIR"))

print(len(names))
print(names)
print(names[0])

print(names1)
print(names[0])
print(names[1])


if "AKBAR" in names:
    print("Yes Akbar in the list")
else:
    print("NOT IN THE LIST")



# CHANGING LIST ITEMS

names1[1] = "Javed"
print(names1)


# Change multiple names
names1[0:2] = ["Suleman", "Faiz" , "Hameed"]
print(names1)


# Methods

names1.insert(0, "Faheem")
print(names1)

names1.append("Munir")
print(names1)

names1.extend(names)
print(names1)


thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

thislist.remove("apple")
print(thislist)

thislist.pop(1)
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist[2]
print(thislist)


thislist.clear()    # List is been empty after running thus method clear()
print(thislist)     

# LOOPS

fruits = ["Kivi","water_melon","Mangoes","Apple"]
for x in fruits:
    print(x)


for i in range(len(fruits)):
    print(fruits[i])


w = 0
while w < len(fruits):
    print(fruits[w])
    w = w+1


fruits = ["Kivi","water_melon","Mangoes","Apple"]
newfruit = []

for z in fruits:
    if "k" in fruits:
        newfruit.append()
    else:
        print("Error")

    print(newfruit)


# SORT METHOD

fruits.sort()
print(fruits)

num = [100,15,110,55,66,550]
num.sort( reverse = True)
print(num)

num.reverse()
print(num)


myfruits = fruits.copy()
print(myfruits)

# There are several ways to join, or concatenate, two or more lists in Python.
# One of the easiest ways are by using the + operator.

res = fruits + num
print(res)


list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)


# Method	Description
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	    Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list