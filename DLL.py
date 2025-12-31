class Node:
  def __init__(self,data):
    self.prev=None
    self.data=data
    self.next=None

class DLL:
  def __init__(self):
    self.__n=0
    self.__head=None
    self.__tail=None
  def __len__(self):
    return self.__n  
  
  def farword_traverse(self):
    result=""
    curr=self.__head
    while(curr!=None):
      result+=str(curr.data)+"->"
      curr=curr.next
    return result[:-2]
  def backword_traverse(self):
     result=""
     curr=self.__tail
     while(curr!=None):
        result+=str(curr.data)+"->"
        curr=curr.prev
     return result[:-2]
    

  def InsertFromHead(self,data):
        new_node=Node(data)
        new_node.next=self.__head
        self.__head=new_node 
        self.__n+=1
       
  def append(self,data):
    if(self.__head==None):
        # Insert from head
        self.InsertFromHead(data)
        
    else:
      # insert from tail
      new_node=Node(data)
      curr=self.__head
      while(curr.next!=None):
        curr=curr.next
      curr.next=new_node
      new_node.prev=curr
      self.__n+=1
      new_node.prev=curr
      self.__tail=new_node

a=DLL()

a.append(223)
a.append("Hello")
a.append("Hello1")
print(a.backword_traverse())
print(a.farword_traverse())
