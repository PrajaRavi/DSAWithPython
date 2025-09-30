
# import ctypes;
# class MeraList:
#   def __init__(self):
#     # This is condition of an empty list
#     self.size=1 #creating a variable self.size->tell total size of the list
#     self.n=0 #creating a variable self.n->tell total no of elements in the list
#     self.A=self.CreateArray(self.size*2) 
#   def CreateArray(self,capacity):
# # creating an array with size =self.size(capacity) and also it will be a refrential array
#     return (capacity*ctypes.py_object)()
#   def __len__(self):
#     return self.n
#   def append(self,element):
#     # we have actually two cases whenever appending an element inside the  list
#     # first we have enough space in the array then directly append the element 
#     # second we have not enought space in the array then i)create space by doubling the size of the array ii)copy all the data of the preveous array in this new array iii)append the new element
#     if(self.size==self.n):
#       # their is no enough space for append the element
#       # step i)-->creating a double size array
#       B=self.CreateArray(self.size*2)
#       # step ii)-->copy the all elements
#       for i in range(self.n):
#         B[i]=self.A[i]
#       # step iii)--->append the element
#       B[self.n]=element
#       self.A=B
#       self.size*=2
#       self.n+=1
#     else:
#       self.A[self.n]=element
#       # self.A=B
#       self.n+=1
#   def __str__(self):
#     result=''
#     for i in range(self.n):
#        result +=(str(self.A[i]))+','
#     return f"[{result[:-1]}]"   
#   def __getitem__(self,index):
#     if(self.n!=0):
#        return self.A[index]

    
#     else:
#       return []

#   def pop(self):
#     self.n-=1
#     return self.A[self.n]
#   def clear(self):
#     self.n=0
#     self.size=1

#   def find(self,element):
#     if(self.n!=0):
#       for i in range(self.n):
#         if(self.A[i]==element):
#           return i
#       return 'Item Not found'  
#     else:
#       return 'Empty List'
#   def insert(self,index,element):
#    if(self.size==self.n):
#       # their is no enough space for append the element
#       # step i)-->creating a double size array
#       B=self.CreateArray(self.size*2)
#       # step ii)-->copy the all elements
#       for i in range(self.n):
#         B[i]=self.A[i]
#       # step iii)--->append the element
#       for i in range(self.n):
#        if(i==index):
#         for i in range(self.n,index,-1):
#           self.A[i]=self.A[i-1]


#        self.A[index]=element
#       # self.A=B
#        self.n+=1
    
#    else:
#     for i in range(self.n):
#       if(i==index):
#         for i in range(self.n,index,-1):
#           self.A[i]=self.A[i-1]


#         self.A[index]=element
#       # self.A=B
#         self.n+=1
    
# # this magic funciton delitem will be executed whenever [del listName(index)]
#   def __delitem__(self,index):
#     if(index<=self.n and index>=0):
#       for i in range(self.n):
#         if(i==index):
#           for i in range(index,self.n-1,+1):
#             self.A[i]=self.A[i+1]
#           self.n-=1  
#     if(index>self.n or index<0):     
#       print("Index doesn't exist")
#   def remove(self,item):
#     if(self.n!=0):
#       for i in range(self.n):
#         if(self.A[i]==item):
#           for j in range(i,self.n-1,+1):
#               self.A[j]=self.A[j+1]
#           self.n-=1
#     else:
#        print('Empty list')  
#CREATING SORT FUNCTIONALITY------------------->
  # def sort(self):
  #   result=''
  #   for i in range(self.n):
  #     # print(type(self.A[i]))
  #     result+=str(type(self.A[i]))
      
  #   print(result) 
  #   if("<class 'str'>" in result and "<class 'int'>" in result):
  #     # print('str') 
  #     print("sort method can't be applied on a list containing both int and str")
  #   elif("<class 'str'>" in result and not "<class 'int'>" in result):
  #     print('str')
      
  #   else:
  #     # sorting all the integers
  #     for i in range(self.n):

  #     # print('int')


# l1=MeraList()
# l1.append(4)
# l1.append(4)
# l1.append('Hello')
# l1.append('Hello1')
# l1.append('Hello')
# print(len(l1))    
# print(l1)
# print(l1.pop())

# print(l1)
# l1.clear()
# print(l1.find(4))
# l1.insert(0,'Ravi')
# print(l1)
# del l1[-1]
# l1.remove(4)
# l1.remove(4)
# l1.remove('Hello')
# l1.remove('Hello1')
# l1.sort()
# l1.remove('Hello1')

# print(l1)
# print(l1[0])


# class Node:
#   def __init__(self,data):
#     self.data=data #this is data part
#     self.next=None #this is address part
# class LinkedList:
#   def __init__(self):
#     #now initially we will create an empty linked list as well as any object of this class is made
#     # condition of an empty LL
#     self.head=None
#     self.n=0 #this will tell us total no of elements(Node) inside our LL

#   def __len__(self):
#       return (self.n)
#   def InsertFromHead(self,item):
#     new_node=Node(item)
#     new_node.next=self.head#matlab hum pura Node hi new_node.next me store kar rahe hai overall we are storing the address of the head node
#     self.head=new_node
#     self.n+=1
#   def __str__(self):
#     result=''
#     curr=self.head#means curr variable me maine head wale node ko store kiya hoon
#     while(curr!=None):
#       result+=str(curr.data)+'->'
#       # print(curr.data)
#       curr=curr.next
#     return f"{result[:-2]}" 
#   def append(self,item):
#     if(self.n!=0):
#       curr=self.head
#       new_node=Node(item)
#       while(curr.next!=None):
#         curr=curr.next
#       # now my curr element is the last node
#       curr.next=new_node
#       self.n+=1
#       return
    
#     self.InsertFromHead(item)  
#     # basically add the given item after the element maintioned
#   def InsertAfter(self,afteritem,additem):
#     # i)traverse to the afteritem
#     curr=self.head
#     new_node=Node(additem)
#     while(curr!=None):
#       if(curr.data==afteritem):
#         #  print(curr.data)
#          new_node.next=curr.next
#          curr.next=new_node
#          self.n+=1
#          return
#       curr=curr.next
#     print('Item Not found')  
#   def clear(self):
#     self.head=None
#     self.n=0
#   def DeleteFromHead(self):  
#    if(self.n!=0):
#     curr=self.head
#     #  curr.next=None
#     self.head=curr.next
#     self.n-=1
#    else:
#      print('Linked List is empty Now',end='')
#   def pop(self):
#     if(self.n>1):
#       curr=self.head
#       while(curr.next.next!=None):
#         curr=curr.next
#       curr.next=None
#       self.n-=1  
#     else:
#       self.DeleteFromHead()
#   def remove(self,item):
#     curr=self.head
#     if(curr.data==item):
#       self.DeleteFromHead()
#     elif(self.n==0):
#       print('Empty Linked List')

#     else:
#       while(curr.next!=None):
#         if(curr.next.data==item):
#           curr.next=curr.next.next 
#           self.n-=1
#           break
        
#         curr=curr.next  
#   def find(self,item):
#     count=0
#     curr=self.head
#     while(curr!=None):
#       if(curr.data==item):
#         print(f'{item} found at index {count}')
#         return
#       count+=1
#       curr=curr.next

#     print(f'{item} Not found in this Linked List')  # self.pop()

#   def findwithindex(self,index):
#     count=0
#     curr=self.head
#     while(curr!=None):
#       if(index==count):
#         print(curr.data)
#         return
#       count+=1
#       curr=curr.next
#     print('Item Not found')  
#     # adding indexing feature
#   def __getitem__(self,index):
#     self.findwithindex(index)

#     # function to find max value in linked list which contain only whole numbers and also replace this number by a given number
#   def findMaxValue(self,item):
#     max=self.head.data
#     curr=self.head
#     while(curr.next!=None):
#       if(max<curr.data):
#         max=curr.data
#         curr.data=item
#       curr=curr.next
#     print(max)


#   # function to find sum of all the odd positioned element in the linked list
#   def SumOfOdd(self):
#     sum=0
#     count=0
#     curr=self.head
#     while(curr!=None):
#       if(count%2!=0):
#         sum+=curr.data
#       curr=curr.next
#       count+=1
#     print(sum)  
# # function to reverse a linked list using the same linked list means you can't create a new linked list(in place reversal)
#   def reverse(self):
#     curr_node=self.head
#     # initially considering prev_node to be None
#     prev_node=None
#     while(curr_node!=None):
#       next_node=curr_node.next
#       curr_node.next=prev_node#here we are making the head node a tail node
#       prev_node=curr_node
#       curr_node=next_node
#     self.head=prev_node  
# # function to solve wordlist problem------------------>
#   def ChangWordList(self):
#     curr=self.head
#     while(curr!=None):
#       if(curr.data=='/' or curr.data=='*'):
#          curr.data=' '
#          if(curr.next.data=='*' or curr.next.data=='/'):
#            curr.next.data=' '
#            curr.next.next.data=curr.next.next.data.upper()  
#            curr=curr.next.next
#       curr=curr.next
  
# l1=LinkedList()
# l1.InsertFromHead(34)
# l1.InsertFromHead(3)
# l1.InsertFromHead('Hello')
# l1.InsertFromHead('Hello1')
# l1.append('Hello13')
# l1.append(45)
# l1.append(455)
# l1.append(4)
# l1.append(5)
# l1.append(25)
# l1.append(35)
# l1.SumOfOdd()

# making wordlist
# for this in str method replace -> by ' '
# l1.append('T')
# l1.append('h')
# l1.append('e')
# l1.append('/')
# l1.append('*')
# l1.append('s')
# l1.append('k')
# l1.append('y')
# l1.append('*')
# l1.append('*')
# l1.append('i')
# l1.append('s')
# l1.append('/')
# l1.append('/')
# l1.append('b')
# l1.append('l')
# l1.append('u')
# l1.append('r')
# l1.append('*')
# l1.append('*')
# l1.append('h')
# l1.append('e')
# l1.append('l')
# l1.append('l')
# l1.append('o')
# print(l1)
# l1.ChangWordList()
# print(l1)
# l1.reverse()

# l1.findMaxValue('Hello')
# l1.InsertAfter('Hello','Ravi')
# l1.clear()
# l1.DeleteFromHead()
# l1.DeleteFromHead()
# l1.DeleteFromHead()
# l1.DeleteFromHead()
# l1.DeleteFromHead()
# l1.DeleteFromHead()
# l1.DeleteFromHead()
# l1.DeleteFromHead()
# l1.remove(34)
# l1.remove(45)
# l1.remove('Hello1')
# l1.remove('Hello')
# l1.find('Hello')
# l1.findwithindex(3)
# l1.remove('Hello1')
# l1[3]
# print(l1)
# print(len(l1))


#<----------------------- CREATING A STACK CLASS USING LINKEDLIST----------------------------------------->


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
  def ReverseString(self,string):
    revstr=''
    for i in range(len(string)):
      self.push(string[i])
    for i in range(len(string)):
      revstr+=self.pop()
    print(revstr)

    
  

  def ChangeString(self,string,pattern):
     for i in string:
       s1.push(i)
     for i in pattern:
       if(i=='u'):
         s2.push(s1.pop())
       if(i=='r'):
         s1.push(s2.pop()) 
     curr=self.Top
     result=''
     while(curr!=None):
      #  print(curr.data)
       result=str(curr.data)+result
       curr=curr.next
     print(result)


s1=Stack()   
s2=Stack()   
# s1.push('Hello')   
# s1.push('Hello1')   
# s1.push('Hello12')   

# s1.ChangeString('Ravi','uuurrr')


# <--------------------SOLVING THE CELEBRITY PROBLEM----------------------------------------->
# l=[
#   [0,1,1,1],#0
#   [0,0,0,0],#1
#   [0,1,1,0],#2
#   [0,1,1,0],#3
# ]
# def findTheCeleb(l):
#   # print(l)
#   s=Stack()
#   for i in range(len(l)):
#     # print(i)
#     s.push(i)
#   while(s.size()>=2):
#     i=s.pop()#3
#     j=s.pop()#2
#     if(l[i][j]==0):
#       # i j ko nahi janta means j can't be a celebrity
#       s.push(i)
#     else:
#      # i j ko janta hai means i can't be a celebrity
#      s.push(j)
#   #when this loop will be end then we have only one element in this stack and we have only two options now
#   # i)celebrity is the element inside the stack
#   # ii)celebrity is None  
#   celeb=s.pop()
#   for i in range(len(l)):
#     if(i!=celeb):
#       if(l[i][celeb]==0 or l[celeb][i]==1):
#         print('No one is celebrity')
#         return

#   print('celebrity is ',celeb)
# findTheCeleb(l)




# <----------------------------BALANCED PARANTHESIS--------------------------------------->

# mystr='(a+b)('
# def BalancedParanthesis(mystr):
#   s=Stack()
#   for i in mystr:#i=[,{,(
#    if(i=='[' or i=='{' or i=='('  ):
#       s.push(i)
      
    
#    elif(i==']' and s.n!=0):
#      if(s.peek()=='['):
#         s.pop()
#      else:
#        print('false')  
       
       
#    elif(i=='}' and s.n!=0):
#      if(s.peek()=='{'):
#         s.pop()
#      else:
#        print('false')  
        

#    elif(i==')' and s.n!=0):
#      if(s.peek()=='('):
#         s.pop()
#      else:
#        print('false')  
       
#    elif((i==')' or i=='}' or i==']') and s.n==0):
#      print('false')   
     
#   if(s.n==1):   
#     print('false')     

# BalancedParanthesis(mystr)






# <-------MAKING A STACK USING ARRAY  SINCE IN PYTHON WE DONT HAVE ANY ARRAY BUT LIST IN PYTHON CAN BE  USED AS Array ---------->
# class Stack():
#   # since we are creating a stcack using Array and in python we are using List insted of Array hence here list have a fix size just like an array in c and c++ also it is defined as the time of declaration
#   def __init__(self,size):
#     self.size=size
#     self.stack=[None]*self.size
#     self.top=-1
#   def push(self,item):
#     if(self.top==self.size-1):
#       print("Overflow")
#     else:
#       self.top+=1
#       self.stack[self.top]=item 
#   def pop(self):
#     if(self.top!=-1):
#       # print(self.top)    
#       print(self.stack[self.top])
#       self.top-=1
#     else:
#       print("Empty Stack")
#   def __str__(self):
#     result=''
#     for i in range(self.top+1):
#       result+=str(s.stack[i])+', '
#     return f'[{result[:-2]}]'
#       # print(s.stack[i])
# s=Stack(3)  
# print(s.stack)
# s.push(12)
# s.push(1)
# s.push(13)

# # s.pop()
# # s.pop()
# # s.pop()
# # s.pop()
# # s.push(139)
# print(s)
# # print(s.stack)




# <---------------------QUES-------------------------------->
# we will create a ques using concept of  Linked List
# class Node:
#   def __init__(self,value):
#     self.data=value
#     self.next=None
# class Queue:
#   def __init__(self):
#   #condition of an empty queue
#    self.front=None#head
#    self.rear=None#tail
#   def enque(self,item): 
#     new_node=Node(item)
#     if(self.rear==None):
#       # queue is empty
#       self.front=new_node
#       self.rear=new_node
#     else:
#      #their is some element already in this queue  
#     #  here we will do insertion from tail
#       self.rear.next=new_node
#       self.rear=new_node
#   def deque(self):
#     if(self.front==None):
#      #queue is empty
#      print('Empty queue',end='') 
#     else:
#     #delete node from head
#      self.front=self.front.next
#   def size(self):
#     count=0
#     curr=self.front
#     while(curr!=None):
#       count+=1
#       curr=curr.next
#     print(count)  
#   def __str__(self):
#     result=''
#     curr=self.front
#     while(curr!=None):
#       result+=str(curr.data)+' '  
#       curr=curr.next
#     return result[:-1]
#   def front_item(self):
#     curr=self.front
#     while(curr.next!=None):
#       curr=curr.next     
#     print(curr.data)  

#   def tail_item(self):
#     curr=self.front
#     print(curr.data)  
# q=Queue() 
# q.enque(12) 
# q.enque(13) 
# q.enque(14) 
# q.deque() 
# q.size()
# q.front_item()
# q.tail_item()
# # q.deque() 
# # q.deque() 
# # q.deque() 
# print(q)

# class Queue:
#   s1
#   s2
#   def __init__(self):
#     self.n=s2.size()
#   def enque(self,item):    
#     s1.push(item)
#     self.n+=1
#   def __str__(self):
#     return (str(self.n))
      
#   def deque(self):
#     if(s2.size()==0):
#        if(s1.size!=0):
#         for i in range(self.n):  
#           s2.push(s1.pop())

#           # s2.size()-=1
#         # print(s2)  
#        else:
#          print("Que is empty Now")
#     else:
#       s2.pop()  
#       # s2.size()-=1    
#       self.n-=1
          
# q=Queue()
# q.enque(12)
# q.enque(13)
# q.enque(14)
# q.deque()
# q.deque()
# q.deque()
# q.deque()
# q.deque()
# q.deque()
# print(q)
# print(s2.size())
# print(s1.size())
# print(s1)




#<------------- we have to make a dictionary class using hash functions which will act same as dictionries in python----------------->
# first we will be using {concept of linear probing(easy as compare to channing)}
# <---------------for this problem refer any other python text editor because in vs code we got each time a diffrent hash value of any immutable data type--------------------->
# class Dictionry:
#   def __init__(self,size):
#     self.size=size
#     self.slots=[None]*self.size
#     self.data=[None]*self.size
#   def put(self,key,value):
#     #here we got the index of the key
#     hash_value=self.hash_function(key)
#     #now we have two possibility i)the index position is empty ii)the index position is already filled
#     if(self.slots[hash_value]==None):
#       #case i
#       self.slots[hash_value]=key
#       self.data[hash_value]=value
#     else:
#       # it also have two possibilty i)the filled element is the element which i want to insert ii)the filled element is diffrent from the element which i want to insert
#       # case i)
#       if(self.slots[hash_value]==key):
#         self.data[hash_value]=value
#       else:
#         #case ii)
#         #now we will search that next index postion is empty or not(Linear Probing)
#         #now since we have to move to next index postion so we have to calculate hashvalue again for the key
#         new_hash_value=self.rehash(hash_value)
#         #now again two possibity i)the next index postion is empty ii)the next positon is already filled in this case the linear probing will be continued so we have to use loop for this
#         while(self.slots[new_hash_value]!=None and self.slots[new_hash_value]!=key):#basically loop will end after the last element of the slots array
#           new_hash_value=self.rehash(new_hash_value)
#         #Now again two possibility i) when i reached on next index then no item stored ii)already an item is stored
#         if(self.slots[new_hash_value]==key):
#           print('key wala break hai')
#           self.data[new_hash_value]=value
#         else:
#           print('None wala break')
#           self.slots[new_hash_value]=key
#           self.data[new_hash_value]=value

#   def rehash(self,old_hash):
#     return (old_hash+1)%self.size   

#   def hash_function(self,key):
#     hashed_value=abs(hash(key))
#     return hashed_value%self.size
#   def __setitem__(self,key,value):
#     self.put(key,value)
#   def __getitem__(self,key):
#     # total 3 cases i)item mil gaya ii)item nahi mila(matlab same index per vapas aa gaye) iii)item nahi mila(we got an item with key None)
#     start_position=self.hash_function(key)
#     curr_position=start_position
#     while(self.slots[curr_position]!=None):
#       if(self.slots[curr_position]==key):
#         # item mill gaya
#         return self.data[curr_position]
#       curr_position=self.rehash(curr_position)
#       if(curr_position==start_position):
#         return "Item Not found(same index per vapas a gaya)"
#       if(curr_position==None):
#         return "Item Not found(None wala)"

# D1=Dictionry(3) 
# print(D1.slots)
# print(D1.data)
# D1['python']=12
# D1['java']=123
# # D1['php']=13
# # D1.put('python',23)
# # D1.put('java',24)
# # D1.put('php',247)
# # D1.put('python',2300)
# # Basically when we are adding more key value pair inside our dictionry then it goes on infinite loop solution->we have to increse the size of the array
# # D1.put('c',200)
# # print(D1['hello'])
# print(D1.slots)
# print(D1.data)



























