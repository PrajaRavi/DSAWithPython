class Node:
  def __init__(self,data):
    self.data=data #this is data part
    self.next=None #this is address part
class LinkedList:
  def __init__(self):
    #now initially we will create an empty linked list as well as any object of this class is made
    # condition of an empty LL
    self.head=None
    self.n=0 #this will tell us total no of elements(Node) inside our LL

  def __len__(self):
      return (self.n)
  def InsertFromHead(self,item):
    new_node=Node(item)
    new_node.next=self.head#matlab hum pura Node hi new_node.next me store kar rahe hai overall we are storing the address of the head node
    self.head=new_node
    self.n+=1
  def __str__(self):
    result=''
    curr=self.head#means curr variable me maine head wale node ko store kiya hoon
    while(curr!=None):
      result+=str(curr.data)+'->'
      # print(curr.data)
      curr=curr.next
    return f"{result[:-2]}" 
  def append(self,item):
    if(self.n!=0):
      curr=self.head
      new_node=Node(item)
      while(curr.next!=None):
        curr=curr.next
      # now my curr element is the last node
      curr.next=new_node
      self.n+=1
      return
    
    self.InsertFromHead(item)  
    # basically add the given item after the element maintioned
  def InsertAfter(self,afteritem,additem):
    # i)traverse to the afteritem
    curr=self.head
    new_node=Node(additem)
    while(curr!=None):
      if(curr.data==afteritem):
        #  print(curr.data)
         new_node.next=curr.next
         curr.next=new_node
         self.n+=1
         return
      curr=curr.next
    print('Item Not found')  
  def clear(self):
    self.head=None
    self.n=0
l=LinkedList()
l.append(45)
l.append(55)
l.append(56)
print(l)