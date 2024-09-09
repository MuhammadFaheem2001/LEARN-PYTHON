# WHILE LOOP 


i = 0

while i < 10:
    print(i)
    i = i+1



i = 0

while i < 10:
    if i == 3:
        print("Arrive at 3")
        i = i+1
    else:
        print(i)
        i = i+1



i = 0

while i < 10:
    if i == 3:
        print("Arrive at 3")
        break    # THE CONDITION STOP AT 3
      #  continue  # THE CONDITION ALSO RUN
    else:
        print(i)
        i = i+1




# FOR LOOP

fruit = ["Banana","Apple","Mango"]

for x in fruit:
    print(x)


fruit = ["Banana","Apple","Mango"]

for x in fruit:
    print(x)
    if "Banana" in x:
        print("Yes")
    else:
        print("False")



fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)


for x in range(6):
    print("Python is easy")

for x in range(2, 50):
    print(x)



for x in range(6):
  print(x)
else:
  print("Finally finished!")



# First is starting point
# Second is Limit
# Third is gap

for x in range(0 , 1000 , 100):
    print(x)


adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)



a = ["Apple", "Banana", "Mango"]
b = ["Cherry", "Water_melon", "Nashpati"]

for x in a:
    for y in b:
        print( a  , " VS " , b)



# FUNCTION



def first_fuc():
    operator = input("Enter Your Operator (+,-,*,/,%): ")
    inp = int(input("Enter Your Number: "))
    inp1 = int(input("Enter Your Number: "))
    
    if operator == "+":
        print("The value of Sum " ,inp + inp1) 
    elif operator == "-":
        print("The value of Subtraction " ,inp - inp1)
    elif operator == "*":
        print("The value of Mutiplication " ,inp * inp1)
    elif operator == "/":
        print("The value of Division " ,inp / inp1)
    elif operator == "%":
        print("The value of Remainder " ,inp % inp1)
    else:
        print("This operation can't exist in this program")
        
        
first_fuc()





def greet(Name):
    print("Hello " + Name)
    
    
greet("Faheem")



def Vote_Eligiblity():
    
    Age = int(input("Enter your Age: "))

    if Age >= 18 and Age <= 60:
        print("You are eligible for voting")
    elif Age > 60:
        print("You are old citizen you can vote from home")
    elif Age < 18:
        print("You are not eligible for voting")
    else:
        print("You Ruinned the Program")
        
    
Vote_Eligiblity()



def Multiplication(a, b):
    
    print("The value of A * B is: " , a * b)
        
    
Multiplication(10, 5)