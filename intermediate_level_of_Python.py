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





