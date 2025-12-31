class Node:
  def __init__(self,value):
    self.data=value
    self.next=None

class Ques:
  def __init__(self):
    self.__n=0
    self.__front=None
    self.__rear=None
    
  def enque(self,data):
    new_node=Node(data)
    if(self.__n==0):
      self.__front=new_node
      self.__rear=new_node
      self.__n+=1
    else:
      self.__rear.next=new_node  
      self.__rear=new_node
      self.__n+=1
  def deque(self):
    if(self.__n==0):
      return
    curr=self.__front
    self.__front=curr.next
    self.__n-=1  
  def front_item(self):
    if(self.__n==0):
      return "empty"
    return self.__front.data
  def rear_item(self):
    if(self.__n==0):
      return "empty"
    return self.__rear.data
  def size(self):
    return self.__n
  def __str__(self):
    mystr=""
    curr=self.__front
    while(curr!=None):
      mystr=mystr+curr.data+"->"
      curr=curr.next
    return (f"[{mystr[:-2]}]")

q=Ques()
# q.enque("hello")
# q.enque("I")
# q.enque("am")
# q.enque("Ravi")
# q.enque("Prajapati")
print(q)
print(q.front_item())
print(q.rear_item())
# print(q.size())





