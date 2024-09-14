# Pandas is a Python library.
# Pandas is used to analyze data.

import pandas as pd

# a = pd.read_csv('data.csv')
# print(a.to_string())


data = {
    "Car": ["Audi", "BMW", "VOLVO"],
    "Price": [12000, 13000, 8000]
}

var = pd.DataFrame(data)
print(var)
print(pd.__version__)


# A Pandas Series is like a column in a table.
# It is a one-dimensional array holding data of any type.

b = [1,2,3,4,5,6,7,8,9,10]
var1 = pd.Series(b)
print(var1)
print(var1[0])



c = [1,2,3]
var2 = pd.Series(c, index=["X","Y","Z"])
print(var2)
print(var2["Z"])



calories = {"Day1":100 ,"Day2": 200,"Day3": 300,}
var3 = pd.Series(calories)
print(var3)


calories = {"Day1":100 ,"Day2": 200,"Day3": 300,}
var3 = pd.Series(calories, index=["Day1", "Day3"])
print(var3)



data1 = {

    "Calories": [100,500,300,1100],
    "Duration": [50,30,40,60]
}

var4 = pd.DataFrame(data1)
print(var4)
print(var4.loc[0])
print(var4.loc[[0, 1]])




data2 = {
    "Name":          ["Faheem","Shahid","Kashif"],
    "Age":           [22,36,35],
    "Occupation":    ["Student","Consultant","Govt_Emp"],
    "Marital_Status":["Single","Married", "Single"]
}

var5 = pd.DataFrame(data2, index = ["NO.1", "NO.2", "NO.3"])
print(var5)


read = pd.read_csv("data.csv")
print(read)