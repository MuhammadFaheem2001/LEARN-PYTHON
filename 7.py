# TUPLES 

# Tuples are used to store multiple items in a single variable.
# Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

tup = ("Set", "List" , "Dictionary")
print(len(tup))
print(tup[0])
print(tup[1:2])
print(tup[-2])
print(type(tup))
print(tup)

tup1 = (1) 
tup2 = ("Faheem")
tup3 = (3.24)
tup5 = ("BSCS")
tup4 = (1 , "Faheem" , "BSCS", 3.25)

print( "ID" , tup1 , "Name" + tup2  +  " Program " + tup5  + "CGPA" , tup3)


# Tuple is not accessable now we first convert it into the list than change the data inside tuple then after updating the list we convert it into the 
# tuple using list(variable_name) , tuple(variable_name) we can also use the list methods

tup6 = ("Salman","Sharukh","Tufail","Yaqoob")
lis = list(tup6)
lis[0] = "Muhammad"
list[1] = "Tufail"
list[2] = "Muhammad"
list[3] = "Yaqoob"

print(lis)
print(type(lis))
print(len(lis))




fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)


thistup = ("Juniad","Akram","Jamshed")
for x in thistup:
    print(x)



thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1



tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)


fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)



# Method	Description
# count()	Returns the number of times a specified value occurs in a tuple
# index()	Searches the tuple for a specified value and returns the position of where it was found
