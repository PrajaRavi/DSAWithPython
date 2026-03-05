class Node:
  def __init__(self,data):
    self.left=None
    self.right=None
    self.data=data
    
   

class BST:
  def __init__(self):
    self.__size=0
    self.__root=None
    self.__flag=False
    self.check=False
  def just(self):
    curr=self.__root
    print(curr.left.right.data,"left") #40
    print(curr.right.right.data,"right") #450  
  def __len__(self):
    return self.__size
  def RootNode(self):
    return self.__root
  
  def MinValueOfSubTree(self,node):
    if(node==None): 
      return 
    curr=node
    while(curr.left!=None):
      curr=curr.left
    return curr  
  
  def MaxValueOfSubTree(self,node):
    if(node==None):
      return 
    curr=node
    while(curr.right!=None):
      curr=curr.right
    return curr
  def PreOrderTrav(self,node):
    if(node==None):
      return
    print(node.data,end=", ")
    self.PreOrderTrav(node.left)
    self.PreOrderTrav(node.right)
    
  def InOrderTrav(self,node):
    if(node==None):
      return
      
    self.InOrderTrav(node.left)
    print(node.data,end=", ")
    self.InOrderTrav(node.right)
    

  def PostOrderTrav(self,node):
    if(node==None):
      return
    self.PostOrderTrav(node.left)
    self.PostOrderTrav(node.right)
    print(node.data,end=", ")
  
  def ItemExistOrNOt(self,node,item):
    if(node==None):
      return 
    self.ItemExistOrNOt(node.left,item)
    if(node.data==item):
      self.check=True
      return 
     
    self.ItemExistOrNOt(node.right,item)

  # Insertion using recursion
  def Insert(self,data):
    self.__root=self.rInsert(self.__root,data)      
  def rInsert(self,root,data):
    if(root is None):
      return Node(data)
    elif(data<root.data):
      root.left=self.rInsert(root.left,data)
    elif(data>root.data):
      root.right=self.rInsert(root.right,data)
    return root

     
  # Code for delete using recursion
  def delete(self, key):
        self.__root = self._delete(self.__root, key)

  def _delete(self, root, key):
        if root is None:
            return None

        # 🔍 Search the node
        if key < root.data:
            root.left = self._delete(root.left, key)

        elif key > root.data:
            root.right = self._delete(root.right, key)

        else:
            # 🎯 Node found

            # CASE 1: No child (leaf node)
            if root.left is None and root.right is None:
                return None

            # CASE 2: One child
            if root.left is None:
                return root.right

            if root.right is None:
                return root.left

            # CASE 3: Two children           
            # Find inorder successor (smallest in right subtree) 
            # or find predesisor
            
            successor = self._minValueNode(root.right) 
            
            root.data = successor.data #here we are replacing the deleted element with it's successor
            root.right = self._delete(root.right, successor.data) #and here we are deleting the successor 
        return root


  def _minValueNode(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
   

    
      
    
     
      
  #My Insertion Logic using if else ladder
  # def Insertion(self,data):
  #   new_node=Node(data)
  #   if(self.__root==None):
  #     self.__root=new_node
  #     self.__size+=1
  #   else:
  #     if(data<self.__root.data):
  #       if(self.__root.left==None):
  #         self.__root.left=new_node 
  #         self.__size+=1
  #       else:
  #         curr=self.__root.left
  #         while(curr.left!=None):
  #           curr=curr.left  
  #         #now we are at last left node
  #         if(data>curr.data):
  #           new_curr=curr
  #           while(new_curr.right!=None):
  #             new_curr=new_curr.right
  #           new_curr.right=new_node
  #           self.__size+=1
  #         else:
  #           new_curr=curr
  #           while(new_curr.left!=None):
  #             new_curr=new_curr.left
  #           new_curr.left=new_node
  #           self.__size+=1    
          
  #     else:
  #       if(self.__root.right==None):
  #         self.__root.right=new_node    
  #         self.__size+=1
  #       else:
  #         curr=self.__root.right
  #         while(curr.right!=None):
  #           curr=curr.right
  #         #now we are at last right node
            
  #         if(data>curr.data):
  #           new_curr=curr
  #           while(new_curr.right!=None):
  #             new_curr=new_curr.right
  #           new_curr.right=new_node
  #           self.__size+=1
  #         else:
  #           new_curr=curr
  #           while(new_curr.left!=None):
  #             new_curr=new_curr.left
  #           new_curr.left=new_node
  #           self.__size+=1  

tree=BST()
tree.Insert(40)
tree.Insert(30)
tree.Insert(50)
tree.Insert(60)
tree.Insert(20)
tree.Insert(10)
tree.Insert(80)
tree.Insert(45)
tree.InOrderTrav(tree.RootNode())
      








