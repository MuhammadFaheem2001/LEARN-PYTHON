import pandas as pd


pd.options.display.max_rows = 9999
read = pd.read_csv("data.csv")
print(read)
print(read.to_string())
print(pd.options.display.max_rows)




# Read JSON
# Big data sets are often stored, or extracted as JSON.

# JSON is plain text, but has the format of an object, and is well known in the world of programming, including Pandas.


read1 = pd.read_json("data1.json")
print(read1)
print(read1.to_string())

# CREATE A JSON FILE

data = {
    "Duration": {
       "01": 25, 
       "02": 54, 
       "03": 12, 
       "04": 21, 
       "05": 32, 
       "06": 70, 
       "07": 12, 
       "08": 34 
    },

    "Pulse": {
       "01": 120, 
       "02": 130, 
       "03": 150, 
       "04": 90, 
       "05": 50, 
       "06": 70, 
       "07": 60, 
       "08": 150 
    },

    "Maxpulse": {
       "01": 200, 
       "02": 300, 
       "03": 400, 
       "04": 500, 
       "05": 600, 
       "06": 700, 
       "07": 800, 
       "08": 900 
    },

    "Calories": {
       "01": 755, 
       "02": 451, 
       "03": 455, 
       "04": 551, 
       "05": 544, 
       "06": 145, 
       "07": 777, 
       "08": 771
    }
}

var2 = pd.DataFrame(data)
print(var2)



read2 = pd.read_csv("data.csv")
print(read2.head(80))


read3 = pd.read_csv("data.csv")
print(read2.tail(20))              # If we don't assign tail or head value it will assign randomly 5   



read4 = pd.read_csv("data.csv")
print(read4.head())

read5 = pd.read_csv("data.csv")
print(read5.tail())


print(read1.info())
print(read2.info())
print(read3.info())
print(read4.info())
print(read5.info())


