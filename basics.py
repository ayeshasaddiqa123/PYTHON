# 1. Write a program to print Twinkle twinkle little star poem in python.

print ("""Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky""")



# 2. Install an external module and use it to perform an operation of your interest.

import pyjokes
jokes=pyjokes.get_jokes()
print (jokes)



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






