class Node :
    """create left and right  nodes"""
    def __init__(self , data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree :
    """Create binary tree and their left to right nodes"""
    def __init__(self):
        self.root = None

    def create(self):
        """Create binary tree in which each node has one or two chid ratheer than leaf node"""
        val = int(input("Enter value (-1 for no node) : "))

        if val == -1:
            return None

        new_node = Node(val)

        print("Enter left child of node " , val)
        new_node.left = self.create()


        print("Enter right child of node " , val)
        new_node.right = self.create()

        return new_node

    def inorder(self , root) :
        """Inorder traversal of binary tree"""
        if root :
            self.inorder(root.left)
            print(root.data , end = " ")
            self.inorder(root.right)
    
    def preorder(self , root) :
        
     if root :
        print(root.data , end = " ")
        self.preorder(root.left)
        self.preorder(root.right)

    def postorder(self , root) :
     if root :
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.data , end = " ")
        
        






bt = BinaryTree()
print("Create binary tree ")
bt.root = bt.create()


print("Inorder traversal")
bt.inorder(bt.root)

print("\nPreorder traversal")
bt.preorder(bt.root)

print("\nPostorder traversal")
bt.postorder(bt.root)


# Inorder traversal
# 3 4 2 5 1 7 6 8
# Preorder traversal
# 1 2 3 4 5 6 7 8
# Postorder traversal
# 4 3 5 2 7 8 6 1