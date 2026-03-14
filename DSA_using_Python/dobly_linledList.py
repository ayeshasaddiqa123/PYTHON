class Node: # Define a node of the doubly linked list
    def __init__(self, roll):
        self.roll = roll
        self.prev = None
        self.next = None

class DoublyLinkedList: # Define the doubly linked list
    def __init__(self):
        self.head = None

#    Insert a new node at the end of the list
    def insert_at_end(self, roll):
        new_node = Node(roll)
        
        if self.head == None :
            self.head = new_node
        else :
            temp = self.head 
            while temp.next is not None :
                temp = temp.next
                
            temp.next = new_node
            new_node.prev = temp
    def insert_at_begin(self ,roll) :
        new_node = Node(roll)
        if self.head == None :
            self.head = new_node
        else :
            temp = self.head
            self.head = new_node
            new_node.next = temp    
            temp.prev = new_node
            
    def delete_at_begin(self):
        temp = self.head 
        temp.next.prev = None
        self.head = temp.next
        del temp        
    # def insert_at_location(self, roll, loc) :
        
    #     if self.head == None :
    #         self.head = new_node
    #     else : 
    #         temp = self.head
    #         while temp.next is not None :
    #             if temp.roll == loc :
    #                 break
    #             temp = temp.next
    #     new_node = Node(roll)
    #     new_node.next = temp.next
    #     new_node.prev = temp
    #     temp.next = new_node
    #     new_node.prev = temp  
                
    def display(self) :
        temp = self.head
        while temp is not None :
            print(temp.roll , "<--->" ,end ="")
            temp = temp .next 
            
                   
    def backwardTraversal(self) :
        temp = self.head
        while temp.next is not None :
            temp = temp.next 
        while temp is not None :
            print(temp.roll , "<--->" ,end ="")
            temp = temp.prev
            
            
        
                
d = DoublyLinkedList()
  
d.insert_at_begin(5)
d.insert_at_end(10)
d.insert_at_end(20)
d.insert_at_end(30)
d.display() 
print("\nAfter deletion") 
d.delete_at_begin()
d.display()
print("\nBackward") 
d.backwardTraversal()
             
# d.insert_at_location(25,20)
# d.display()