# 1. Write a program to print Twinkle twinkle little star poem in python.

print ("""Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky""")


#-------------------------------------------------------------------------

# 2. Install an external module and use it to perform an operation of your interest.

import pyjokes
jokes=pyjokes.get_jokes()
print (jokes)


#----------------------------------------------------------------------------

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