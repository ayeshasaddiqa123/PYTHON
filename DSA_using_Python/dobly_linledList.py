class Node: # Define a node of the doubly linked list
    def __init__(self, roll):
        self.roll = roll
        self.prev = None
        self.next = None

class DoublyLinkedList: # Define the doubly linked list
    def __init__(self):
        self.head = None

    def insert(self, roll): # Insert a new node at the end
        new_node = Node(roll)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last

    def insert_begin(self, roll): # Insert a new node at the beginning
        new_node = Node(roll)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def insert_end(self, roll): # Insert a new node at the end
        self.insert(roll)

    def insert_location(self, roll, position): # Insert a new node at a specific position
        new_node = Node(roll)
        if position == 0:
            self.insert_begin(roll)
            return
        temp = self.head
        for _ in range(position - 1):
            if temp is None:
                print("Position out of bounds")
                return
            temp = temp.next
        new_node.next = temp.next
        new_node.prev = temp
        if temp.next:
            temp.next.prev = new_node
        temp.next = new_node


    def delete_begin(self): # Delete a node from the beginning
        if self.head is None:
            print("Nothing to delete")
            return
        self.head = self.head.next
        if self.head:
            self.head.prev = None

    def delete_end(self): # Delete a node from the end
        if self.head is None:
            print("Nothing to delete")
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        if temp.prev:
            temp.prev.next = None
        else:
            self.head = None        


    def delete_location(self, position): # Delete a node from a specific position
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        if position == 0:
            self.delete_begin()
            return
        for _ in range(position):
            if temp is None:
                print("Position out of bounds")
                return
            temp = temp.next
        if temp is None:
            print("Position out of bounds")
            return
        if temp.next:
            temp.next.prev = temp.prev
        if temp.prev:
            temp.prev.next = temp.next

    def search(self): # Search for a value in the list
        if self.head is None:
            print("List is empty")
            return
        val = int(input("Enter value to search: "))
        temp = self.head
        found = False
        while temp:
            if temp.roll == val:
                found = True
                break
            temp = temp.next
        if found:
            print("Value found in the list")
        else:
            print("Value not found in the list")


    def display(self): # Display the list
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        while temp:
            print(f"{temp.roll} <-> ", end="")
            temp = temp.next
        print()

l1 = DoublyLinkedList()

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
           l1.insert(roll)
        

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