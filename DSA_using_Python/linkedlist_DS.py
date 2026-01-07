class New_Node:

    def __init__(self,roll,name):
        self.roll=roll
        self.name=name
        self.next=None

class Linkedlist:
    def __init__(self):
        self.head = None

    def insert (self,roll,name):
        node=New_Node(roll,name)

        if self.head == None:
            self.head=node
            
        else:

            temp=self.head
            while(temp.next != None):
                temp = temp.next
            temp.next=node


    def display(self):
        if self.head == None:
            print("List is empty \n Nothing to display.....")
        else:
            temp=self.head
            while temp is not None:
                print(f"Roll no is {temp.roll} Name is {temp.name}")
                temp=temp.next
            
               
    def insert_begin(self):

        roll=int(input("Enter roll no:"))
        name=input("Enter name :")
        node=New_Node(roll,name)
        if self.head == None:
            self.head=node
        else:
            temp=node
            temp.next=self.head
            self.head=node

    def insert_end(self):
         
         roll=int(input("Enter roll no:"))
         name=input("Enter name :")
         node=New_Node(roll,name)
         if self.head == None:
            self.head=node
         else:
             temp=self.head
             while(temp.next is not None):
                 temp=temp.next
             temp.next=node    

    def delete_begin(self) :
        if self.head == None :
            print("Nothing to delete")
        else:
            self.head=self.head.next

    def delete_end(self):
        if self.head == None :
            print("Nothing to delete")
        else:
            temp=self.head
            while temp.next.next is not None:
                temp=temp.next
            last=temp.next
            temp.next=None
            del last

    def delete_location(self):
        if self.head==None:
            print("List is empty")
        else:
            val=int(input("Enter value which you want to delete : "))            
            temp=self.head
            prev=None
            found=False
            while(temp is not None):
                if temp.roll == val:
                    found=True
                    break
                prev=temp
                temp=temp.next
            if found:
                if prev is None:
                    self.head=self.head.next
                else:
                    prev.next=temp.next
                del temp
            else:
                print("Value not found ")


    def insert_location(self):
        if self.head==None:
            print("List is empty")
        else:
            pos=0
            val=int(input("Enter value where you want to insert : "))            
            temp=self.head
            while(temp.next is not None):
                if temp.roll == val:
                    pos=-1
                    break
                temp=temp.next
            if (pos==-1):
                roll=int(input("Enter roll no:"))
                name=input("Enter name :")
                node=New_Node(roll,name)
                node.next=temp.next
                temp.next=node

            else:
                print("Value not found ")    
            
    def search(self):
        if self.head==None:
            print("List is empty")
        else:
            val=int(input("Enter value which you want to search : "))            
            temp=self.head
            found=False
            while(temp is not None):
                if temp.roll == val:
                    found=True
                    break
                temp=temp.next
            if found:
                print(f"Value {val} is found ")
            else:
                print("Value not found ")







l1=Linkedlist()
loop=1
while(loop==1):
    print("01 . Create a list list")
    print("02 . Insert node in beginning")
    print("03 . Insert node at end")
    print("04 . Insert node at specific location")
    print("05 . Delete node from beginning ")
    print("06 . Delete node from end ")
    print("07 . Delete node from specific location ")
    print("08 . Search value from node ")
    print("09 . display ")
    print("10 . Exit")
    option=int(input("Enter your option : "))
    if option==1:
       
       for i in range(0,3):
           roll=int(input("Enter roll no:"))
           name=input("Enter name :")
           l1.insert(roll,name)
        

    elif option==2:
        l1.insert_begin()
    elif option==3:
        l1.insert_end()
    elif option==4:
        l1.insert_location()
    elif option==5:
        l1.delete_begin()
    elif option==6:
        l1.delete_end()
    elif option==7:
        l1.delete_location()
    elif option==8:
        l1.search()
    elif option==9:
        l1.display()
    elif option==10:
        print("Exiting....")
        loop=0
    else:
        print("Invalid option ")







    


    


