# OBJECT ORIENTED PROGRAMMING


# Python Classes/Objects

# Python is an object oriented programming language.
# Almost everything in Python is an object, with its properties and methods.
# A Class is like an object constructor, or a "blueprint" for creating objects.


# Classes

class Val:
    x = 5

p1 = Val.x
print(p1)



class Person():
    def __init__(self , Name , Age):
        self.Name = Name
        self.age = Age

per1 = Person("Faheem", 22)

print(str(per1.Name) + " is very good at programming and his Age is " + str(per1.age))
print(per1.Name)
print(per1.age)



class Person1():
    def __init__(self ,fname ,lname):
        self.fname = fname
        self.lname = lname

    def __str__(self):
        return f"My first Name is {self.fname} and My last Name is {self.lname}"

per2 = Person1("Muhammad","Faheem")


print(per2.fname)
print(per2.lname)




class Family():
    def __init__(self , Name , FatherName):
        self.Name = Name
        self.FatherName = FatherName

    def myfunc(self):
        print("My name is " + str(self.Name) + " and my father name is " + str(self.FatherName))

per3 = Family("Faheem" , "Naeem")
per3.myfunc()

print(per3.FatherName, per3.Name)



class call():
    def __init__(obj , Naam , WalidNaam):
        obj.Naam = Naam
        obj.WalidNaam = WalidNaam

    def func(obj2):
        print("My Name is " + str(obj2.Naam) + " and my Father Name is " + str(obj2.WalidNaam))


per4 = call("Faheem" , "Naeem")
per4.func()

per4.Naam = "Muhammad Faheem"
per4.WalidNaam = "Muhammad Naeem Akhtar"
print(per4.Naam)
print(per4.WalidNaam)