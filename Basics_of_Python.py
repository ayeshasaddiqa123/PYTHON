

            We can print any type of text in double quotes by using print function but it is restricte
    to only single line at a time. 
      print("Hello , here is a best way to learn  python")

            Multi line text can printed using triple double quotes as given below.

# 1. Write a program to print Twinkle twinkle little star poem in python.

print ("""Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky""")


            We can use external pieces of code (modules) to use in our own program and don't need to
    write them own. We can install them by using command "pip install -------" in terminal as I installed "pip install pyjokes" given below.       

# 2. Install an external module and use it to perform an operation of your interest.

import pyjokes
jokes=pyjokes.get_jokes()
print (jokes)

Here are some popular external Python modules (also called third-party libraries):

1. NumPy – Numerical operations, arrays  
2. Pandas – Data analysis and manipulation  
3. Matplotlib – Data visualization  
4. Seaborn – Statistical data visualization  
5. Scikit-learn – Machine learning  
6. TensorFlow – Deep learning  
7. Keras – High-level neural networks  
8. PyTorch – Deep learning  
9. OpenCV – Image and video processing  
10. Requests – HTTP requests  
11. BeautifulSoup – Web scraping  
12. Flask – Lightweight web framework  
13. Django – Full-stack web framework  
14. SQLAlchemy – Database ORM  
15. Pygame – Game development  
16. SymPy – Symbolic math  
17. Plotly – Interactive plots  
18. FastAPI – High-performance web APIs  
19. NLTK – Natural language processing  
20. Spacy – Industrial NLP  
21 .requests: HTTP requests and web APIs
22.Pillow: Image processing
23.lxml: XML and HTML processing
24.pytest: Testing framework



These need to be installed separately using pip (e.g., pip install numpy).




1. Built-in Modules (Standard Library)
These come pre-installed with Python. Example:
- os
- sys
- math
- datetime
- random
- json
- re
- itertools
- functools
- time
- typing
- collections
- subprocess

Below is an example of built in module :-

# 3. Write a python program to print the contents of a directory using the os module.

import os

# Specify the desired directory path
directory_path = "D:/PYTHON"  # Change this to your desired path

# List and print all files and folders in the specified directory
contents = os.listdir(directory_path)
print(f"Contents of the directory '{directory_path}':")
for item in contents:
    print(os.path.join(directory_path, item))
 

 -----------------------------------------------------------------------------

  
  Variables are the named memory locations..The values stored in variables can be changed.
  RULES FOR CHOOSING AN IDENTIFIER 
• A variable name can contain alphabets, digits, and underscores. 
• A variable name can only start with an alphabet and underscores. 
• A variable name can’t start with a digit. 
• No while space is allowed to be used inside a variable name. 
Examples of a few variable names are: harry, one8, seven, _seven etc.

data types deine a set of value and set of operations on those values.
Here’s a list of common data types used in Python:

1. Numeric Types
- int – Integer (e.g., 5, -3)
- float – Floating-point number (e.g., 3.14)
- complex – Complex number (e.g., 2 + 3j)

2. Sequence Types
- str – String (e.g., "Hello")
- list – List (e.g., [1, 2, 3])
- tuple – Tuple (e.g., (1, 2, 3))
- range – Range (e.g., range(5))

3. Set Types
- set – Set (e.g., {1, 2, 3})
- frozenset – Immutable set

4. Mapping Type
- dict – Dictionary (e.g., {'a': 1, 'b': 2})

5. Boolean Type
- bool – Boolean (True or False)

6. Binary Types
- bytes – Immutable bytes
- bytearray – Mutable bytes
- memoryview – Memory view object

7. None Type
- NoneType – Represents the absence of value (None)


OPERATORS IN PYTHON 
Following are some common operators in python: 
1. Arithmetic operators: +, -, *, / etc. 
2. Assignment operators:  =, +=, -= etc. 
3. Comparison operators: ==, >, >=, <,  != etc. 
4. Logical operators: and, or, not. 


#  1. Write a python program to add two numbers. 

a=int(input("enter number :"))
b=int(input("enter number :"))
print (a+b)

# 2. Write a python program to find remainder when a number is divided by z.
a=int(input("enter number :"))
b=int(input("enter number :"))
print("Remainder of both are :" , a%b)

# 3. Check the type of variable assigned using input () function. 
c=input("Enter value : ")
print(type(c))

 
# 4. Use comparison operator to find out whether ‘a’ given variable a is greater than 
# ‘b’ or not. Take a = 34 and b = 80 
a=34
b=80
print  ( "Is that relation true :" , a>b )
# 5. Write a python program to find an average of two numbers entered by the user. 
 
a=int(input("enter number :"))
b=int(input("enter number :")) 
print ("average is :" , (a+b)/2)

# 6. Write a python program to calculate the square of a number entered by the user. 

a=int(input("enter number :"))
print ("square  is :" , a**2 )



------------------------------------------------------------------------

        String is a data type in python.It is immutable.It cannot be changed once it is declared.
    The string can be sliced to get a part of it.
    There are three ways to represent a string :
    a='Ayesha'
    b="Ayesha"
    c='''Ayesha'''
    syntax to slice:
                    e.g. of  variable "a"
                    sl=a[0:3]
                    print(sl)
                    The output is : Aye
      we can also get single element of it as : p= a[1]
       output will: y             
              
Following are the methods of strings:


1. str.upper() – Converts to uppercase  
2. str.lower() – Converts to lowercase  
3. str.capitalize() – Capitalizes first letter  
4. str.title() – Title-case  
5. str.swapcase() – Swaps case  
6. str.strip() – Removes leading/trailing spaces  
7. str.lstrip() – Removes left spaces  
8. str.rstrip() – Removes right spaces  
9. str.replace(old, new) – Replaces substring  
10. str.find(sub) – Finds index of first occurrence  
11. str.rfind(sub) – Finds last occurrence  
12. str.index(sub) – Like find() but raises error if not found  
13. str.count(sub) – Counts occurrences  
14. str.startswith(sub) – Checks if starts with  
15. str.endswith(sub) – Checks if ends with  
16. str.split(sep) – Splits into list  
17. str.rsplit(sep) – Splits from the right  
18. str.join(iterable) – Joins list into string  
19. str.isalpha() – Checks if all characters are letters  
20. str.isdigit() – Checks if all digits  
21. str.isalnum() – Letters and digits  
22. str.isspace() – All spaces  
23. str.isupper() – All uppercase  
24. str.islower() – All lowercase  
25. str.istitle() – Title case check  
26. str.zfill(width) – Pads with zeros
27. str.center(width) – Centers string  
28. str.ljust(width) – Left-aligns  
29. str.rjust(width) – Right-aligns  
30. str.partition(sep) – Splits into 3 parts (before, sep, after)  
31. str.rpartition(sep) – From right  
32. str.encode() – Converts to bytes  
33. str.casefold() – Aggressive lowercase (better for comparisons)



# 1. Write a python program to display a user entered name followed by Good 
# Afternoon using input () function. 
name = input("Enter name:")
print (f"Good After noon {name} ")




# 2. Write a program to fill in a letter template given below with name and date. 
letter = '''  
Dear <|Name|>, 
You are selected! 
<|Date|> 
''' 
print(letter.replace ( "<|Name|>" , "Ayesha").replace("<|Date|> " , "12 september"))




# 3. Write a program to detect double space in a string. 
name="Ha  rry"
print(name.find("  "))


# 4. Replace the double space from problem 3 with single spaces. 
name="Ha  rry"
print(name.replace("  "," "))



# 5. Write a program to format the following letter using escape sequence 
# characters. 
# letter = "Dear Harry, this python course is nice. Thanks!" 
letter = "Dear Harry,\n  \t this python course is nice.\n Thanks!"
print(letter)


# 6. use all functions of strings in an example
str=" Ayesha , you are the best "
print( str.upper())
print(str.lower())
print( str.capitalize() )
print(str.title())
print(str.swapcase())
print(str.strip())
print(str.lstrip())
print(str.rstrip())
print(str.replace(" Ayesha , you are the best ","Saad"))
print(str.find("are"))
print(str.rfind("Ayesha"))
print(str.index("you"))
print(str.count("a"))
print(str.startswith(" Ayesha"))
print(str.endswith("best "))
print(str.split())
print(str.rsplit())
print("_".join(str))
print(str.isalpha())
print(str.isdigit())
print(str.isalnum())
print(str.isspace())
print(str.isupper())
print(str.islower())
print(str.istitle())
print("7".zfill(5))
print("hi".center(8))
print("hi".ljust(8,"-"))
print("hi".rjust(8,"-"))
print(str.encode())
print(str.casefold())
result1 = str.partition("you")
print("partition():", result1)
result2 = str.rpartition("the")
print("rpartition():", result2)


-------------------------------------------------------------------------------


# 1. Write a program to store seven fruits in a list entered by the user. 

list = ["Peach" , "Apple" , "orange" , "Pineapple", "Banana" , "Mango" , "pear"]
print(list)
# 2. Write a program to accept marks of 6 students and display them in a sorted 
# manner.
marks=[30,40,60,70,32,65]
marks.sort()
print(marks) 

OR 

marks = []

f1 = int(input("Enter Marks here: "))
marks.append(f1)
f2 = int(input("Enter Marks here: "))
marks.append(f2)
f3 = int(input("Enter Marks here: "))
marks.append(f3)
f4 = int(input("Enter Marks here: "))
marks.append(f4)
f5 = int(input("Enter Marks here: "))
marks.append(f5)
f6 = int(input("Enter Marks here: "))
marks.append(f6)

marks.sort()

print(marks)


# 3. Check that a tuple type cannot be changed in python. 
a = (34, 234, "Harry")

 a[2] = "Larry"  # it would give error
print (a)


# 4. Write a program to sum a list with 4 numbers. 

a = (34, 234, 32)

print(sum(a))




# 5. Write a program to count the number of zeros in the following tuple: 
a = (7, 0, 8, 0, 0, 9) 

print (a.count(0))






-----------------------------------------------------------------------------------------------------------


# Write a program in python make the calculator when the input the values and operation.

a=int(input("Enter a number :"))
b=int(input("Enter a number :"))
print("Sum of entered numbers is : ",a+b)
c=int(input("Enter  number :"))
d=int(input("Enter  number :"))
print ("Difference of entered numbers is :",c-d)
e=int(input("Enter  number :"))
f=int(input("Enter  number :"))
print("Product of enterd numbers is :",e*f)
g=int(input("Enter a number :"))
h=int(input("Enter  number :"))
print("Remainder is :",g%h)
i=int(input("Enter number :"))
j=int(input("Enter  number :"))
print("Diviion of enterd numbers is :",i/j)




# Write a program show the leap year when the user enter the year.
year=input("Enter year : ")
print(year , " is leap year.")


# Write a Python program that takes 5 numbers as input, stores them in a list, and then prints the largest number.
list=[]
a=int(input("Enter number here :"))
list.append(a)
b=int(input("Enter number here :"))
list.append(b)
c=int(input("Enter number here :"))
list.append(c)
d=int(input("Enter number here :"))
list.append(d)
e=int(input("Enter number here :"))
list.append(e)
print(max(list))

# Write a Python program to check if a number entered by the user is positive, negative, or zero.
a=int(input("Enter number to check wether it is positive  :"))
print(a>0 )
a=int(input("Enter number to check wether it is negative :"))
print(a<0)
a=int(input("Enter number to check wether it is zero :"))
print(a==0)

Write a program using Append .
list=[1,2,3,4]
list.append(3)
print(list)


# Write a program that user entered the six name of fruits you can store in the index
list = []
list.append(input("Enter fruit 1: "))
list.append(input("Enter fruit 2: "))
list.append(input("Enter fruit 3: "))
list.append(input("Enter fruit 4: "))
list.append(input("Enter fruit 5: "))
list.append(input("Enter fruit 6: "))
print("Fruits entered:", list)




# Print the list of STRING's FUCTIONs.(6-10) .
name ="ayesha"
print(name.endswith("ha"))
print(name.startswith("ay"))
print(name.capitalize())
print(name.lower())
print(name.upper())
print(name.strip())
print(name.lstrip())
print(name.isalpha())
print(name.islower())
print(name.isupper())
print(name.isalnum())
print(name.split(','))

print(len(name))


# How can you find the data type of int, float, string, Boolean, none ?
a=int(input("Enter any desired number you want to check the type of data :"))
print(type(a))
a=float(input("Enter any desired number you want to check the type of data :"))
print(type(a))
a=input("Enter any desired number you want to check the type of data :")
print(type(a))
a=bool(input("Enter any desired number you want to check the type of data :"))
print(type(a))



# Write a program that user can enter the roll no of student after that the record of the student will show in output {roll no (1-5)}.
list=[]
a=int(input("Enter rollno here :"))
list.append(a)
b=int(input("Enter rollno here :"))
list.append(b)
c=int(input("Enter rollno here :"))
list.append(c)
d=int(input("Enter rollno here :"))
list.append(d)
e=int(input("Enter rollno here :"))
list.append(e)
print(list)

# Write a Python program that take 5 numbers from the user. Store them in a list. Print only the even numbers from the list.


list=[]
a=int(input("Enter number here :"))
list.append(a)
b=int(input("Enter number here :"))
list.append(b)
c=int(input("Enter number here :"))
list.append(c)
d=int(input("Enter number here :"))
list.append(d)
e=int(input("Enter number here :"))
list.append(e)
print( list[0]%2==0 )
print( list[1]%2==0)
print( list[2]%2==0)
print( list[3]%2==0)
print( list[4]%2==0)



------------------------------------------------------------------------------------------------------------------
