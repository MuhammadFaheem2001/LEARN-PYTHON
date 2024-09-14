import pandas as pd

read = pd.read_csv("data.csv")
read.corr()
print(read)



read2 = pd.read_json("data1.json")
var = read2.corr()
print(var.to_string())


# Pandas Ploting

# Pandas uses the plot() method to create diagrams.
# We can use Pyplot, a submodule of the Matplotlib library to visualize the diagram on the screen.


import pandas as pd
import matplotlib.pyplot as mt

read3 = pd.read_csv("data.csv")
read3.plot()

mt.show()


read4 = pd.read_csv("data.csv")
read4.plot(kind="scatter" , x="Calories", y="Duration") # Before writing the name of kind just make "" you can see all options

mt.show()