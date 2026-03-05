class Node():
  def __init__(self,data):
    self.prev=None
    self.data=data
    self.next=None
    
class DCLL(): #->Doubly circular linked list
  def __init__(self):
    self.__n=0
    self.__head=None
  def InsertFromHead(self,data):
    if(self.__head==None):
      new_node=Node(data)
      self.__head=new_node
      self.__n+=1
    else:
      new_node=Node(data)
      new_node.next=self.__head
      self.__head.prev=new_node
      self.__head=new_node
      self.__n+=1
      
  def farwordTraverse(self):
    print(self.__head.data)

a=DCLL()
a.InsertFromHead(23)
a.InsertFromHead(230)
a.InsertFromHead(2300)
a.farwordTraverse()
      