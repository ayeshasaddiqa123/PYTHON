
Dictionary:
          It is a collection of keys value pairs.
Benefit :
        Easy lookup.
        it is unordered.
        it is unindexed
        Cannot conain duplicate values.

        Here are all the commonly used dictionary methods in Python:

clear() – Removes all items from the dictionary.
copy() – Returns a shallow copy of the dictionary.
fromkeys(seq[, value]) – Creates a new dictionary from a sequence of keys and a value.
get(key[, default]) – Returns the value for key if key is in the dictionary, else default.
items() – Returns a view object of (key, value) pairs.
keys() – Returns a view object of the dictionary’s keys.
pop(key[, default]) – Removes the specified key and returns the value.
popitem() – Removes and returns the last (key, value) pair.
setdefault(key[, default]) – Returns the value of key. If key does not exist, inserts key with a value of default.
update([other]) – Updates the dictionary with elements from another dictionary or from an iterable of key-value pairs.
values() – Returns a view object of the dictionary’s values.

here is the dictionary's values:


        marks = {
    "Harry": 100,
    "Shubham": 56,
    "Rohan": 23,
    0: "Harry"
}
print(marks.popitem())
print(marks.items())
print(marks.keys())
print(marks.values())
print(marks.copy())
print(marks.clear())
# print(marks.fromkeys("Rohan",23))
a=marks.setdefault("Rohan")
print(a)
marks.update({"Harry":90,"Ayesha":100})
print(marks)
print(marks.values())


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


Set:
    A set is a  collection of well defined disinct 

Here are methods used on sets:

    add(elem) : Adds an element to the set.
clear() : Removes all elements from the set.
copy() : Returns a shallow copy of the set.
difference(*others) : Returns the difference of sets as a new set.
difference_update(*others) : Removes all elements of another set from this set.
discard(elem) : Removes an element if it is a member. Does nothing if not present.
intersection(*others) : Returns the intersection of sets as a new set.
intersection_update(*others) : Updates the set with the intersection of itself and others.
isdisjoint(other) : Returns True if two sets have a null intersection.
issubset(other) : Returns True if another set contains this set.
issuperset(other) : Returns True if this set contains another set.
pop() : Removes and returns an arbitrary set element. Raises KeyError if empty.
remove(elem) : Removes an element. Raises KeyError if not present.
symmetric_difference(other) : Returns the symmetric difference as a new set.
symmetric_difference_update(other) : Updates the set with the symmetric difference.
union(*others) : Returns the union of sets as a new set.
update(*others) : Updates the set with the union of itself and others.


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



~--------------------------------------------------------------------------------------------------------------------------------------------------


# WRITE A PROGRAM IN PYTHON THAT MAKE THE ATM MACHINE /JAZZCASH PROGRAM APPLICATION……
# 1 You set the password. 
# 2 show 4 option.
#    i-Account balance
#   ii-Send money (username ,amount mention and date)
#   iii- Received cash( sender name, account holder name and amount how much?)
# iv-After deposit check balance how much increase balance in your Account
# For example::
# when user enter the option 1 “send money” you gave the info about send money process after all process. Show output send money successfully (account holder, receiver name, cash and date



balance=25000
password=int(input("Enter Password :"))
 
if(password==0000):
    print("1.Check Account balance \n 2.Send money (username ,amount mention and date)\n 3. Received cash( sender name, account holder name and amount how much?)\n 4.After deposit check balance how much increase balance in your Account")
    c=int(input("Enter your choice:"))
else:
    print("Wrong password ..........")
    

if(c==1):
    print("Your current  account balance is ",balance)
    
elif(c==2):
    print("Enter name of that person you want to send money:")
    user_name=input()
    print("How much amount do you want to send :")
    amount=int(input())
    if(amount < balance  and amount > 0):
        print ( "Rs." , amount ," are transferred successfully to " , name , "from Ayesha Saddiqa's account" , "dated 7/29/2025")
    else:
        print("Your account has no sufficient money.........recharge it")    
    
 

elif(c==3):
    sender_name = input("Enter sender's name: ")
    account_holder = input("Enter your account holder name: ")
    amount = int(input("Enter amount received: "))
    balance += amount
    print(f"Rs. {amount} received from {sender_name} to {account_holder}.")
    print(f"Your new account balance is Rs. {balance}")


 
elif(c==4):
    print("How much money you want to deposit :")
    amount=int(input())
    print("After depositing money your balace is rs:",amount+balance)


 

    

---------------------------------------------------------------------------------------------------------

#To print members of list using while loop

list=[1,2,"Ayesha","Irfan"]

i=0

while(i<len(list)):
    print(list[i])
    i=i+1



#To print members of list using for loop
list=[1,2,"Ayesha","Irfan"]

for i in list:
    print(i)
    i+=1


# To print members of list using for loop
t=(1,2,3,4)

for i in t:
    print(i)

# To print members of stringlist using for loop and else also

s="Ayesha"
for i in s:
    print(i)
else:
    print("Done")    


# break and continue 
for i in range(100):
    if(i==5):
        break
    print(i)


for i in range(100):
    if(i==5):
        continue
    print(i)


---------------------------------------------------------------------------------------------------------------------------------------------------------

# 1. Write a program to print multiplication table of a given number using for loop. 
num=int(input("Enter number :"))
for i in range(1,11):
    print(num , "*" ,i ,"=" ,num*i)
    i+=1





# 2. Write a program to greet all the person names stored in a list ‘l’ and which starts 
# with S.
list=["Ayesha","Sachan","Usman","Irfan"]

for name in list:
    if(name.startswith("S")):
        print("Hello",name)


# 3. Attempt problem 1 using while loop. 
num=int(input("Enter a number to print the table of it :"))
i=1
while(i<11):
    print(f"{num}*{i}={num*i}")
    i+=1




# 4. Write a program to find whether a given number is prime or not. 

n=int(input("Enter a number :"))

for  c in range(1,n):
    if(n%c==0):
        print(n," is a composite number.")
        break
else:
        print(n," is a prime number. ")    




# 5. Write a program to find the sum of first n natural numbers using while loop. 
n=int(input("Enter a number:"))
i=0
sum=0
while(i<=n):
    sum=sum+i
    i+=1
print("Sum is :",sum)




# 6. Write a program to calculate the factorial of a given number using for loop. 

n=int(input("Enter a number:"))
f=1
for i in range(1,n+1):
    f=f*i
    i=i+1
print("Factorial is :",f)



# 7. Write a program to print the following star pattern. 
# * 
# *** 
# ***** for n = 3

n=int(input("Enter a number :"))

for i in range(1,n+1):
    print(" "*(n-i) ,end="")
    print("*"*(2*i-1),end="")
    print("\n")


# 8. Write a program to print the following star pattern: 
# * 
# ** 
# ***      for n = 3 



n=int(input("Enter a number :"))

for i in range(1,n+1):
   
    print("*"*(i),end="")
    print("")



# 9. Write a program to print the following star pattern. 
# * * * 
# *   *   for n = 3 
# * * *  





n=int(input("Enter a number :"))

for i in range(1,n+1):
    if(i==1 or i==n ):
       print("*"*(n),end="")
    else:
        print ("*" ,end="")
        print (" " *(n-2),end="")
        print ("*" ,end="")  
    print("")









# 10. Write a program to print multiplication table of n using for loops in reversed 
# order. 
n=int(input("Enter number:"))

for i in range(1,11):
    print(f"{n}*{11-i}={n*(11-i)}")



--------------------------------------------------------------------------------------------------------

def avg():
    a=int(input("Enter a number :"))
    b=int(input("Enter a number :"))
    c=int(input("Enter a number :"))
    avg=(a+b+c)/3
    print (avg)


avg()


def greet(name,ending="Thanks"):
    print("Good morning ,",name)
    print(ending)
greet("Ayesha","Thankyou")    


def factorial(n):
    if(n==0 or n==1):
        return 1
    return n*factorial(n-1)


n=int(input("Enter a number:"))
print("Fatorial of " ,n , "is : ",factorial(n))



---------------------------------------------------------------------------------------------------------
# 1. Write a program using functions to find greatest of three numbers. 
def max():
    a=int(input("Enter a number :"))
    b=int(input("Enter a number :"))
    c=int(input("Enter a number :"))
    if a>b and a>c  :
        return a
    elif b>a and b>c :
        return b
    else:
        return c        

d= max()
print("The max number is :" , d)

# 2. Write a python program using function to convert Celsius to Fahrenheit. 

def c_to_f():
    c=int(input("Enter temperature in celcius :"))
    f=5*(c-32)/9
    print ("Temperature in farenhiet is :" , f)

c_to_f()




3. How do you prevent a python print() function to print a new line at the end.
print("A",end="") 
print("b",end="") 
print("c",end="") 
print("d",end="") 




4. Write a recursive function to calculate the sum of first n natural numbers. 



def sum(n):
    if(n==1):
        return 1
    return sum(n-1)+ n 
    
n=int(input("Enter the range to which you want to calculate the sum of natural numbers :"))
print ("The sum is :" , sum(n))



5. Write a python function to print first n lines of the following pattern: 
*** 
**               
* - for n = 3 


def pattern(n):
     if(n==0):
        return
     print("*"*n)
     pattern(n-1)   
            

n=int(input("Enter a number :"))
pattern(n)



6. Write a python function which converts inches to cms. 

def inches_to_cms(i):
     return i*2.54

n=float(input("Enter inches to convert it into cms:"))
print("The centimeters are :",inches_to_cms(n))

7. Write a python function to remove a given word from a list and strip it at the same 
time. 


8. Write a python function to print multiplication table of a given number. 







