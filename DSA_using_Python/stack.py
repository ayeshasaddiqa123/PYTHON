# -------------------------------------Stack and its operations-------------------------------------------------------------

class Stack:
    def __init__(self):
        self.stk = []
        self.max_size = 4
        self.top = -1

    def push(self, val):
        if self.top == self.max_size - 1:
            print("Stack Overflow! Nothing can be inserted.")
        else:
            self.stk.append(val)
            self.top += 1
            print(val, "pushed into stack")

    def pop(self):
        if self.top == -1:
            print("Stack Underflow! Nothing to pop.")
        else:
            removed = self.stk.pop()
            self.top -= 1
            print(removed, "popped from stack")

    def display(self):
        if self.top == -1:
            print("Stack is empty")
        else:
            print("Stack elements:")
            for i in range(self.top, -1, -1):
                print(self.stk[i])


st = Stack()
loop = 1

while loop:
    print("\nEnter 1 to push value into stack")
    print("Enter 2 to pop value from stack")
    print("Enter 3 to display values of stack")
    print("Enter 4 to exit")

    option = int(input("Enter your choice: "))

    if option == 1:
        val = input("Enter value: ")
        st.push(val)

    elif option == 2:
        st.pop()

    elif option == 3:
        st.display()

    elif option == 4:
        loop = 0
        print("Program exited")

    else:
        print("Invalid option")



# --------------------------------------conversion of decimal integer into binary form--------------------------------------------------------

class Binary_Conversion :
    def __init__(self):
        self.stk = []
        self.top = -1

    def dec_to_bin (self , num):

        while(num>0):
            remainder = num%2
            self.top += 1
            self.stk.append(remainder)
            num = num//2


    def display(self)->None:
        


        for i in range (self.top, -1, -1):

            print(self.stk[i] , end="")
            

bin = Binary_Conversion()

num = int(input("Enter number to convert it into binary :"))

bin.dec_to_bin(num)

bin.display()


# ---------------------------------------------Reverse a string using stack-------------------------------------------------------------

class Reverse_String :
    def __init__(self):
        self.stk = []
        self.top = -1

    def push_string (self , string):

        for char in string:
            self.top += 1
            self.stk.append(char)


    def reverse_string(self)->None:
        


        for i in range (self.top, -1, -1):

            print(self.stk[i] , end="")


rev= Reverse_String()
string = input("Enter string to reverse it :")
rev.push_string(string)
rev.reverse_string()

