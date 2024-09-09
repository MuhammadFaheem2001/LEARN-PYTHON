# IF ELIF ELSE


a = 10
b = 5 

if a > b:
    print("A is greater than B")
elif b < a:
    print("B is greater than A")
else:
    print("Wrong values")





operator = input("Enter Your Operator (+,-,*,/,%): ")
inp = int(input("Enter the Value: "))
inp1 = int(input("Enter the Value: "))


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



Age = int(input("Enter your Age: "))

if Age >= 18 and Age <= 60:
    print("You are eligible for voting")
elif Age > 60:
    print("You are old citizen you can vote from home")
elif Age < 18:
    print("You are not eligible for voting")
else:
    print("You Ruinned the Program")
