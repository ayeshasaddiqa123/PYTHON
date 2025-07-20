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
 

 #-----------------------------------------------------------------------------



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