# Normal linked list=>1->2->3=>here head is 1 and tail is 3
# reversed linkded list=>1<-2<-3=>here head is 3 and tail is 1
# sorting a linked list 
# method1->using extra space use an extra array copy all the ll element in that array then sort that array and  again push all the element of that array in ll
# method2->merge sort (most efficient method)
# Stacks are just like a linked list where all operation occur from the top(head)

# <-----------------Most efficient method to reverse a string is using slicing---------------------------->
# myword="Ravi"
# print(myword[::-1])

class Node:
  def __init__(self,value):
    self.data=value
    self.next=None

class LL:
  def __init__(self):
    self.__head=None
    self.__n=0
    self.__PN=None
    self.__mylist=[]

  def __len__(self):
    return self.__n
  def InsertFromHead(self,value):
    New_node=Node(value)
    New_node.next=self.__head
    self.__head=New_node
    self.__n+=1 
  def append(self,value):
    if(self.__n!=0):  
      New_node=Node(value)
      curr=self.__head
      while(curr.next!=None):
        curr=curr.next
      curr.next=New_node 
      self.__n+=1 
    else:
      self.InsertFromHead(value)  
  def insert(self,afteritem,value):
    new_node=Node(value)
    curr=self.__head
    while(curr!=None):
      if(curr.data==afteritem):
        # method 1
        # curr_item_add=curr.next
        # curr.next=new_node
        # new_node.next=curr_item_add
        
        # method2
        new_node.next=curr.next
        curr.next=new_node
        self.__n+=1
        return
      curr=curr.next
    print("item not found")
  def clear(self):
    self.__head=None
    self.__n=0  
    print("list is now empty")  
  def DeleteFromHead(self):
    if(self.__head!=None): 
      self.__head=self.__head.next
      self.__n-=1  
    else:
      print("List is empty now",end='')
  def __getitem__(self,index):
    count=0
    curr=self.__head
    while(curr!=None):
      if(count==index):
        return curr.data
      count+=1
      curr=curr.next    
  def pop(self):
    # print(self.__n)
    if(self.__n>=2):  
      curr=self.__head
      while(curr.next.next!=None):
        curr=curr.next
      curr.next=None
      self.__n-=1   
    else:
      self.clear()  
      # print("list is empty now")
  def remove(self,value):

    curr=self.__head

    while(curr.next!=None):
        if(curr.next.data==value ):
          curr.next=curr.next.next
          self.__n-=1
          return
        curr=curr.next    
    if(curr.next==None and curr.data==value):
      self.pop()     
    else:
      print("item not found")  
  def find(self,value):
    count=0
    curr=self.__head
    while(curr!=None):
      if(curr.data==value):
        print(f"item found at index {count}")
        return     
      count+=1
      curr=curr.next
    print("item not found")    
  def __delitem__(self,index):
     count=0
     if(index==0):
       self.DeleteFromHead()
     elif(index==self.__n):
       self.pop()
     else:    
       curr=self.__head
       while(curr!=None):
         if(count==index):
           self.remove(curr.data)
           return
         count+=1
         curr=curr.next
       print(f"the give index {index} not found")  
  def search_index(self,index):
    count=0
    curr=self.__head
    while(curr!=None):
      if(count==index):
        print(f"item with given index is {curr.data}")
        return
      count+=1
      curr=curr.next     
    print(f"item with given index {index} not found")  
  def sort(self):
    # method 1(inefficient since using extra space)
    curr=self.__head
    while(curr!=None):
      self.__mylist.append(curr.data)
      curr=curr.next
    self.__mylist.sort()  
    curr=self.__head
    for i in range(0,len(self.__mylist)):
      curr.data=self.__mylist[i]
      curr=curr.next
  def reverse(self):
   result=""
   curr=self.__head
   while(curr!=None):
     NewNext=curr.next
     curr.next=self.__PN
     self.__PN=curr
     curr=NewNext
   self.__head=self.__PN  



  #  return result

  def __str__(self):
    curr=self.__head
    result=""
    while(curr!=None):
      # print(curr.data)
      result+=(f"{curr.data}->")
      curr=curr.next
    return result[:-2]  
    
          
l=LL()
# l.append(9)
l.append(6)
l.append(7)
l.append(0)
l.append(-10)
l.append(110)
print(l)
l.sort()
print(l)
# print(l.reverse())
# print(l[3])
# l.sort()
# print(l)






