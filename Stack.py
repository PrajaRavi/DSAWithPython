class Node:
  def __init__(self,data):
    self.data=data
    self.next=None
    
class Stack:
  def __init__(self):
    # This is condition of an empty  stack
    self.Top=None
    self.n=0 #it will tell total no of elements in the stack
  def IsEmpty(self):
    # it will return true if stack is empty else false
    if(self.n==0):
      print("True")
    else:
      print("False")
  def push(self,item):
    # it is same as insertFromHead in a LL
    curr=self.Top
    new_node=Node(item)
    new_node.next=curr
    self.Top=new_node
    self.n+=1
    # str method for uuurrr
  # def __str__(self):
  #   curr=self.Top
  #   result=''
  #   while(curr!=None):
  #     result+=str(curr.data)+''
  #     curr=curr.next
  #   return f'{result}'  
  def __str__(self):
    curr=self.Top
    result=''
    while(curr!=None):
      result+=str(curr.data)+'->'
      curr=curr.next
    return f'{result[:-2]}'  
  def size(self):
    return self.n 
  # def peek(self):
  #   if(self.Top==None):
  #     print('Stack is empty ',end='')
  #     return
  #   print(self.Top.data)  




  # peek function in case of Balanced Paranthesis
  def peek(self):
    if(self.Top==None):
      print('Stack is empty ',end='')
      return
    return (self.Top.data)  

  def pop(self):
  #it is same as delete from head in LL
    if(self.Top!=None):
      curr=self.Top
      self.Top=curr.next
      self.n-=1
      return curr.data
    else:
      print("Empty Stack",end='')

s=Stack()

  

