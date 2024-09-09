# String

# To print ant string we use print function with the double quotes "" and character for single quote
print("Hello World")
print("Good bye")


# Shortcuts 

"""
\n  -- for new line
\t  -- for gap between strings 

"""
# String Concatenation
name1 = "Muhammad"
name2 = "Faheem"

print(name1  + " " + name2)


# String slicing 

print(name1[1])
print(name1[0:5])


# Using for loop in String

fruit = "Apple"
for x in fruit:
    print(x)


# Length Keyword

print(len(name1))
print(len(name2))

# Check if any word In the String or missing

something = "I DONT HAVE ANYTHING TO EAT"
print(len(something))
print("apple" in something) # Showing error
print("DONT" in something) 

# In keyword
if "DONT" in something:
    print("Yes it was in the list")
else:
    print("Error")

# Not In keyword 
if "apple" not in something:
    print("Don't have this in String")
else:
    print("ERROR")


# String Slicing

print(name1[0])
print(name1[1])
print(name1[6])
print(name1[2])

print(name1[2:5])
print(name1[0:3])
print(name1[:5])

print(name1[-0:-3])
print(name1[-3:-5])
print(name1[:-3])


# Upper And Lower Cases and other keywords

print(name1.upper)
print(name1.lower)
print(name1.islower)
print(name1.isprintable)
print(name1.isupper)
print(name1.split)
# print(name1.replace("M", "m"))


# String Formating

age = 36
txt = f"My name is John, I am {age}"
print(txt)


# String Methods


"""
Method	            Description
capitalize()	Converts the first character to upper case
casefold()	    Converts string into lower case
center()	    Returns a centered string
count()	        Returns the number of times a specified value occurs in a string
encode()	    Returns an encoded version of the string
endswith()	    Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	        Searches the string for a specified value and returns the position of where it was found
format()	    Formats specified values in a string
format_map()	Formats specified values in a string
index()	        Searches the string for a specified value and returns the position of where it was found
isalnum()	    Returns True if all characters in the string are alphanumeric
isalpha()	    Returns True if all characters in the string are in the alphabet
isascii()	    Returns True if all characters in the string are ascii characters
isdecimal()	    Returns True if all characters in the string are decimals
isdigit()	    Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	    Returns True if all characters in the string are lower case
isnumeric()	    Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	    Returns True if all characters in the string are whitespaces
istitle()	    Returns True if the string follows the rules of a title
isupper()	    Returns True if all characters in the string are upper case
join()	        Joins the elements of an iterable to the end of the string
ljust()	        Returns a left justified version of the string
lower()	        Converts a string into lower case
lstrip()	    Returns a left trim version of the string
maketrans()	    Returns a translation table to be used in translations
partition()	    Returns a tuple where the string is parted into three parts
replace()	    Returns a string where a specified value is replaced with a specified value
rfind()	        Searches the string for a specified value and returns the last position of where it was found
rindex()	    Searches the string for a specified value and returns the last position of where it was found
rjust()	        Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	    Splits the string at the specified separator, and returns a list
rstrip()	    Returns a right trim version of the string
split()	        Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	        Returns a trimmed version of the string
swapcase()	    Swaps cases, lower case becomes upper case and vice versa
title()	        Converts the first character of each word to upper case
translate()	    Returns a translated string
upper()	        Converts a string into upper case
zfill()     	Fills the string with a specified number of 0 values at the beginning

"""