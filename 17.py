# File Handling 

# File handling is an important part of any web application.
# Python has several functions for creating, reading, updating, and deleting files.

# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists
# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)


# Code Starts From Here: 


# f  = open("Faheem.txt" , "w")         Write in the file
# f  = open("Faheem1.txt" , "r")         # Read the File
# f  = open("Faheem1.txt" , "xrwt")    # Create , Read , Write , Text 

# print(f.read())
# print(f.write("Hello This your best friend Faheem"))


z = open("Faheem2.txt", "x")                # Create
z.write("Hello Welcome to this file")       # Write
z.close()                                   # Close


# open and read the file after the appending:

z = open("Faheem2.txt", "r")    # Read
print(z.read())                 # Print


import os

os.remove("Faheem.txt")
os.remove("Faheem1.txt")





import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")



import os
os.rmdir("myfolder")

