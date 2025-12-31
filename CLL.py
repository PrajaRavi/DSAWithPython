# Implementing circular linked list where we kept our pointer at the end because if we keep our pointer at the begining then it will be very less efficient
class Node:
  def __init__(self,data):
    self.data=data
    self.next=None

class CLL:
  def __init__(self):
    self.__tail=None
    self.__n=0

  def __len__(self):
    return self.__n
  def InsertFromTail(self,data):
    if(self.__tail==None):
      new_node=Node(data)
      self.__tail=new_node
      self.__n+=1
    elif(self.__n==1):
      new_node=Node(data)
      temp=self.__tail
      new_node.next=temp
      self.__tail.next=new_node
      self.__tail=new_node
      self.__n+=1
    else:
      new_node=Node(data)
      temp=self.__tail.next
      new_node.next=temp
      self.__tail.next=new_node
      self.__tail=new_node
      self.__n+=1
  def traverse(self):
    curr=self.__tail.next 
    temp=self.__tail.next #->2370
    result=""
    while(temp.data!=curr.next.data): #(2370!=23),(2370!=230)
      result+=str(curr.data)+"->"
      curr=curr.next  #->23,230
    result+=str(curr.data)+"->"
    return result[:-2]  
  def InsertFromHead(self,data):
    new_node=Node(data)
    temp=self.__tail.next
    self.__tail.next=new_node
    new_node.next=temp
    self.__n+=1
  def DeleteFromHead(self):
    temp=self.__tail.next.next
    self.__tail.next=None
    self.__tail.next=temp
    self.__n-=1
    print(self.__tail.next.data)
  def DeleteFromLast(self):
    curr=self.__tail.next 
    temp=self.__tail.next #->2370
    while(temp.data!=curr.next.next.data): #(2370!=23),(2370!=230)
      curr=curr.next  #->23,230
    temp=self.__tail.next
    curr.next=temp
    self.__tail=curr
    


    
a=CLL()
