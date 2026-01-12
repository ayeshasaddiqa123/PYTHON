
class queue:
    def __init__ (self):
        self.f = -1
        self.b = -1
        self.qu = []
        self.size = 3

    def insert(self):
       
        
        for i in range (0,3):
             if self.b == self.size-1 :
               
               print (" Queue is full . ")
               return
             else:
               v=input("Enter value : ")
               self.qu.append(v)
               self.b += 1

               if self.f ==-1:
                   self.f = 0

    def display(self):
        for i in range (self.f,self.b+11):
            print(self.qu[i])               




q=queue()
q.insert()
q.display()



