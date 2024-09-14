# DATA CLEANING


# Data Cleaning
# Data cleaning means fixing bad data in your data set.

# Bad data could be:

# Empty cells
# Data in wrong format
# Wrong data
# Duplicates


import pandas as pd

read = pd.read_csv("data2.csv")
var = read.dropna()
print(var.to_string)


read2 = pd.read_csv("data2.csv")
read2.dropna(inplace= True) #It will remove the null value line
print(read2.to_string)


read3 = pd.read_csv("data.csv")
read3.fillna(130, inplace=True)
print(read3.to_string)

# read4 = pd.read_csv("data2.csv")
# var5=read4["Calories"].fillna(152, inplace=True)
# print(var5.to_string)


# Mean Median Mode

read5 = pd.read_csv("data.csv")
res = read5["Calories"].mean()
read5["Calories"].fillna(res , inplace=True)
print(read5.to_string())



read6 = pd.read_csv("data.csv")
res1 = read5["Calories"].median()
read6["Calories"].fillna(res1 , inplace=True)
print(read6.to_string())



read7 = pd.read_csv("data.csv")
res2 = read7["Calories"].mode()
read7["Calories"].fillna(res2 , inplace=True)
print(read7.to_string())


# read8 = pd.read_csv("data2.csv")
# read8["Date"] = pd.to_datetime(read8["Date"])
# print(read8.to_string())


# read9 = pd.read_csv("data2.csv")
# read9.dropna(subset=["Date"], inplace=True)
# print(read9.to_string())


# Replacing Values

read10 = pd.read_csv("data2.csv")
read10.loc[7, "Duration"] = 45
print(read10.to_string())



for x in read10.index:
  if read10.loc[x, "Duration"] > 120:
    read10.loc[x, "Duration"] = 120


for x in read.index:
  if read.loc[x, "Duration"] > 120:
    read.drop(x, inplace = True)



read11 = pd.read_csv("data.csv")
read11.duplicated()
print(read11)



read12 = pd.read_csv("data.csv")
read12.drop_duplicates(inplace=True)
print(read12)



# Correlation Between data sets

read13 = pd.read_csv("data.csv")
var1 = read13.corr()
print(var1)





