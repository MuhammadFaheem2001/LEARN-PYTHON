# INHERITANCE

class Person():
    def __init__(self , fname, lname):
        self.Fname = fname
        self.Lname = lname
    
    def printname(self):
        print("My name is " + str(self.Fname) + " and my last name is " + str(self.Lname))


p1 =  Person("Muhammad", "Faheem")
p1.printname()
print(p1.Fname, p1.Lname)





class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

x = Student("Mike", "Olsen")
x.printname()








class Car:
   def __init__(self, brand, model):
        self.brand = brand
        self.model = model

        def move():
            print("Moving")

p1 = Car("Mustang", 2024)

print(p1.brand, p1.model)

class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
   
    def Floating():
       print("In the Sear")

p2 = Boat("Submarine", 1523)
print(p2.brand, p2.model)

class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def Fly():
       print("Flying")
    
p3 = Plane("Boeing",2017)
print(p3.brand, p3.model)






class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang") #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747") #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()
