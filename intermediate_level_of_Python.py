car = {

     "Honda": 10,
     "civic": 13,
     "Fortuner": 16,
}

print( car , type(car))
print( "Model of car is : " ,car["Honda"])

car=[["Honda","10"],["Civic","19"]]
print (car[0],type(car))

print(car.items())
print(car.keys())
print(car.values())
car.update({"Honda":14})
print(car)
print(car.get("Honda"))

------------------------------------------------------------------------------


# 1. Write a program to create a dictionary of Hindi words with values as their English 
# translation. Provide user with an option to look it up! 


Words={
    "Qlm":"pencil",
    "churi":"knife",
    "sarana":"pillo",

}
word=input("Enter word to translate it into english :")
print(Words[word])


# 2. Write a program to input eight numbers from the user and display all the unique 
# numbers (once). 
s=set()
n=input("Enter a number :")
s.add(int(n))
n=input("Enter a number :")
s.add(int(n))
n=input("Enter a number :")
s.add(int(n))
n=input("Enter a number :")
s.add(int(n))
n=input("Enter a number :")
s.add(int(n))
n=input("Enter a number :")
s.add(int(n))
n=input("Enter a number :")
s.add(int(n))
n=input("Enter a number :")
s.add(int(n))
print(s)
# 3. Can we have a set with 18 (int) and '18' (str) as a value in it? 
s=set()
s.add(18)
s.add("18")
print(s)
# 4. What will be the length of following set s: 
# s = set() 
# s.add(20) 
# s.add(20.0) 
# s.add('20') # length of s after these operations? 

print(len(s))  
# 5. s = {} 
# What is the type of 's'? 
print(type(s))
The type is dict.
# 6. Create an empty dictionary. Allow 4 friends to enter their favorite language as 
# value and use key as their names. Assume that the names are unique.

d={}


name=input("Enter name :")
lang=input("Enter lang :")
d.update({name:lang})
name=input("Enter name :")
lang=input("Enter lang :")
d.update({name:lang})
name=input("Enter name :")
lang=input("Enter lang :")
d.update({name:lang})
name=input("Enter name :")
lang=input("Enter lang :")
d.update({name:lang})
print(d)



----------------------------------------------------------------------------------------------------------

# . Write a program to find the greatest of four numbers entered by the user. 

a=int(input("Enter number :"))
b=int(input("Enter number :"))
c=int(input("Enter number :"))
d=int(input("Enter number :"))

if(a>b and a>c and a>d):
    print(a , "is greater than all numbers.")
elif(b>a and b>c and b>d):
    print(b , "is greater than all numbers.")
elif(c>a and c>b and c>d):
    print(c , "is greater than all numbers.")
else:
    print(d , "is greater than all numbers.")    

   
# 2. Write a program to find out whether a student has passed or failed if it requires a 
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and 
# take marks as an input from the user. 


sub1=int(input("Enter number :"))
sub2=int(input("Enter number :"))
sub3=int(input("Enter number :"))
 
total_percentage=(100*(sub1+sub2+sub3))/300



if(total_percentage>40  and sub1>33 and sub2>33 and sub3>33 ):
    print("Congrats! you are passed" )

else:
    print("oops! you are failed")
# 3. A spam comment is defined as a text containing following keywords: 
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program 
# to detect these spams.

p1="Make a lot of money "
p2= "buy now"
p3= "subscribe this"
p4="click this"

message=input("Enter comment: ")

if(p1 in message or p2 in message or p3 in message or p4 in message):
    print("This comment is spam")

else:
     print("This comment is not a spam")


# 4. Write a program to find whether a given username contains less than 10 
# characters or not. 
username=input("Enter name :")

if(len(username)>10):
    print("All is well")
else:
    print("Entered username is less than 10 characters.")
     

# 5. Write a program which finds out whether a given name is present in a list or not.
list_of_students=["Ayesha","Ali","Zeeshan","Hussnain","Javeria"]

name=input("Enter name :")

if(name in list_of_students):
    print("The name is in list")
else:
    print("The name is not in list.")  

# 6. Write a program to calculate the grade of a student from his marks from the 
# following scheme: 
# 90 – 100 => Ex 
# 80 – 90 => A 
# 70 – 80 => B 
# 60 – 70  =>C 
# 50 – 60 => D 
# <50 => F
marks=int(input("Enter marks :"))

if(marks>90):
    print("Grade is 'Ex'")
elif(marks>80):
    print("Grade is 'A'")
elif(marks>70):
    print("Grade is 'B'")
elif(marks>60):
    print("Grade is 'C'")
elif(marks>50):
    print("Grade is 'D'")
else:
    print("Grade is 'F'")


# 7. Write a program to find out whether a given post is talking about “Harry” or not. 

post=input("Enter post:")
name=input("Enter name :")

if(name.lower() in post.lower()):
    print("Found")
else:
    print("Not found")   

