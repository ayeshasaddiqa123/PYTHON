
st="Hey i am a good player"

f=open("Myfile.txt","w")
f.write(st)
f.close()



f=open("Myfile.txt")
data=f.read()
print(data)
f.close()



f=open("Myfile.txt")
lines=f.readlines()
print(lines,type(lines))
f.close()



f=open("Myfile.txt")
line1=f.readline()
print(line1,type(line1))

line2=f.readline()
print(line2,type(line2))

line3=f.readline()
print(line3,type(line3))
f.close()




f=open("Myfile.txt")
line=f.readline()

while(line !=""):
    print(line)
    line=f.readline()

f.close()



with open("Myfile.txt") as f:
    print(f.read())





    # . Write a program to read the text from a given file ‘poems.txt’ and find out 
# whether it contains the word ‘twinkle’.

f= open("poems.txt")
content=f.read()
if("Twinkle" in  content):
    print("Present")
else:
    print("Not present") 

f.close() 




