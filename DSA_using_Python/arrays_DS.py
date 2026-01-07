class array:

    def __init__(self):
        self.array = []

    def  insert (self,valu):
        self.array .append(valu) 

    def delete (self,value):

        if value in self .array:
            self.array.remove(value)
            print("value deleted")

        else:
            print ("Value not found in array")        

    def access (self,index):

        if index >= 0 and index < len(self.array):
            return self.array[index]
        
        else:
            return "Index out of bounds"
        

    def search (self,value):
        if value in self.array:
            return self.array.index(value)
        else:
            return None
        
    def display (self):
        return self.array

    def update (self,index,value):

        if index >= 0 and index < len(self.array):
            self.array[index] = value
        else:
            print ("Index out of bounds")

    def size(self):
        return len(self.array)     


a=array()
for i in range (5):
    a.insert(i+1)

print (a.delete(3)) 
print (a.access(1))
print (a.search(4))
print (a.update(2,10))
print (a.size())
print (a.display())



       