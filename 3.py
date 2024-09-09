# NUMBERS


"""
int
float
complex

"""
# Initialization
num0 = 23
num1 = 12.5
num2 = 12j

# Printing Number
print(num0)
print(num1)
print(num2)

#It will print the type of Number:
print(type(num0))
print(type(num1))
print(type(num2))

#INTEGERS
num3 = 12 
num4 = 12348151
num5 = -12542126


print(num3)
print(num4)
print(num5)

print(type(num3))
print(type(num4))
print(type(num5))


#Floats
num6 =  2.5
num7 =  23.5
num8 = -125.5

print(num6)
print(num7)
print(num8)

print(type(num6))
print(type(num7))
print(type(num8))


#COMPLEX
num9  = 2j
num10 = 25j
num11 = -25j


print(num9)
print(num10)
print(num11)

print(type(num9))
print(type(num10))
print(type(num11))

# Number Casting | mean to change the type of integers -> float -> complex by using int(), float(), complex() to any
# other datatype also String....... 
num12 = int(2.2) 
num13 = float(15j)
num14 = complex(12.5)

print(num12)
print(num13)
print(num14)

print(type(num12))
print(type(num13))
print(type(num14))



#Random Numbers

import random

print(random.randrange(50, 100))