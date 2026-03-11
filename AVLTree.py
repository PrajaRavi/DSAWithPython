class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        self.height=1

class AVLTree:
    def __init__(self):
        self.__root=None        
    def getHeight(self,node:Node):
        if(not node):
            return 0
        return node.height

    def getbalancefactor(self,node:Node):
        if(node is None):
            return 0
        return self.getHeight(node.left)-self.getHeight(node.right)

    def right_rotate(self, y:Node):
        """
        Used when the left child is too heavy.
        y is the node that is unbalanced.
        """
        x = y.left
        T2 = x.right

        # Perform rotation
        x.right = y
        y.left = T2

        # Update heights (order matters: update the 'moved' node first)
        y.height =1+  max(self.getHeight(y.left), self.getHeight(y.right)) #This +1 is just for nullsefty overall it has no effect on balancefactor it will just increse height by 1 but diffrance always will be the same
        x.height =1+  max(self.getHeight(x.left), self.getHeight(x.right))

        # Return the new root of this subtree
        return x
    def RootNode(self):
        return self.__root
    
    def left_rotate(self, x:Node):
        """
        Used when the right child is too heavy.
        x is the node that is unbalanced.
        """
        y = x.right
        T2 = y.left

        # Perform rotation
        y.left = x
        x.right = T2

        # Update heights
        x.height =1+  max(self.getHeight(x.left), self.getHeight(x.right))
        y.height =1+  max(self.getHeight(y.left), self.getHeight(y.right))

        # Return the new root
        return y
    def myinsert(self,data):
        self.__root=self.Insert(self.__root,data)
    
    def Insert(self, root:Node, data):
        # 1. Standard BST insertion logic
      
        if not root:
            return Node(data)
        elif data < root.data:
            root.left = self.Insert(root.left, data)
        else:
            root.right = self.Insert(root.right, data)

        # 2. Update the height of the ancestor node
        
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        # 3. Get the balance factor to check if it became unbalanced
        
        balance = self.getbalancefactor(root)
        print(balance)

        # 4. If unbalanced, there are 4 cases:

        # Case 1: Left Left (Single Right Rotation)
        if balance > 1 and data < root.left.data:
            return self.right_rotate(root)

        # Case 2: Right Right (Single Left Rotation)
        if balance < -1 and data > root.right.data:
            return self.left_rotate(root)

        # Case 3: Left Right (Left Rotation on child, then Right Rotation on root)
        if balance > 1 and data > root.left.data:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Case 4: Right Left (Right Rotation on child, then Left Rotation on root)
        if balance < -1 and data < root.right.data:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        
        # self.__root=root
        # print(root.data)
        return root

    def pre_order(self, root):
        if not root:
            return
        print(f"{root.data} ", end="")
        self.pre_order(root.left)
        self.pre_order(root.right)

obj=AVLTree()
obj.myinsert(20)
obj.myinsert(30)
obj.myinsert(12)
obj.myinsert(34)
obj.myinsert(32)
obj.myinsert(31)
print(obj.RootNode().data)
