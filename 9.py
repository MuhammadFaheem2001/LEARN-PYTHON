# DICTIONARY

# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

dic = {
    "First_Name" :  "Muhammad",
    "Last_Name" :  "Faheem",
    "Age" :  22, 
    "DOB" :  "11-12-2001",
    "DOB" : "12-11-2001"        # This new calue will change the value of the DOB
}   

print(dic)
print(type(dic))
print(len(dic))

print(dic["First_Name"])
print(dic["Last_Name"])
print(dic["Age"])
print(dic["DOB"])


dic1 = {
    "Roll_NO"      : 1,
    "Registration" : 55518,
    "Student"      : True,
    "Semester"     : 8
}

print(dic1)
print("Roll_NO: " , dic1["Roll_NO"])
print("Student: " , dic1["Student"])
print("Semester: "  + str(dic1["Semester"]))
print( "Registration: " + dic1["Registration"])



thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)


print(thisdict.keys())


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["year"] = 2020

print(x) #after the change


print(car.get("brand"))
print(car.keys())
print(car.values())
print(car.items())



car1 = {
    "BRAND": "AUDI",
    "MODEL": 2021,
    "YEAR": 2024,
    "YEAR" : 2025, 
    "COLOR": "BLACK"
}


car1["BRAND"] = "MUSTANG"       # THATS HOW WE CHANGE THE DICTIONARY KEY VALUES 
car1.update({"YEAR": 2028})       
car1["COLOR"] = "red"
car1.pop("COLOR")               # NOW IT WILL REMOVE THE COLOR FROM THE DICTIONARY
car1.clear()                    # CLEAR THE DICTIONARY

#print(car1.items())
#print(car1.keys())
#print(car1.values())
#print(car1.get("YEAR"))

# if car1["BRAND"] == "AUDI":     # NOW IT WILL RUN WRONG CODE BLOCK BECAUSE WE CHANGE THE VALUE OF BRAND 
#     print("You are right")
# else:
#     print("Wrong")

for y in car1:
    print(y)
    print(car1[y])




for x,y in car1.items():
    print(x , y)



# NOW COPY CAR1 INTO CAR2

car1 = {
    "BRAND": "AUDI",
    "MODEL": 2021,
    "YEAR": 2024,
    "YEAR" : 2025 
}

car2 = car1.copy()

print(car2)




# NESTED DICTIONARY

dict = {
    "STUDENT1": {
        "Name": "Muhammad_Faheem",    
        "Age": 22,
        "DOB":  "15-12-2006" 
    },
    "STUDENT2": {
        "Name": "ASHRAF_ALI",    
        "Age": 30,
        "DOB": "15-04-1994" 
    },
    "STUDENT3": {
        "Name": "SANDAL_KHATAK",    
        "Age": 15,
        "DOB":  "2010" 
    }
    
}

print(dict)
print(dict["STUDENT1"]["Name"])
print(dict["STUDENT1"])
print(dict["STUDENT1"])






Child1 = {
    "Name": "AKBAR",
    "Age": 22,
    "City": "KARACHI"
}


Child2 = {
    "Name": "HUNAID",
    "Age": 25,
    "City": "ISLAMABAD"
}


Child3 = {
    "Name": "JUNAID",
    "Age": 30,
    "City": "LAHORE"
}

family = {
    "Child1" : Child1,
    "Child2" : Child2,
    "Child3" : Child3,
}

print(family)
print(family["Child1"]["Name"])
print(family["Child2"]["Age"])
print(family["Child3"]["City"])




# Method	        Description
# clear()	        Removes all the elements from the dictionary
# copy()	        Returns a copy of the dictionary
# fromkeys()	    Returns a dictionary with the specified keys and value
# get()	            Returns the value of the specified key
# items()	        Returns a list containing a tuple for each key value pair
# keys()	        Returns a list containing the dictionary's keys
# pop()	            Removes the element with the specified key
# popitem()	        Removes the last inserted key-value pair
# setdefault()	    Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	        Updates the dictionary with the specified key-value pairs
# values()	        Returns a list of all the values in the dictionary







