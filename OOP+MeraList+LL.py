# 1.Algorithmic Complexity--->it is basically all about that how much efficient your code is {for efficeny of a program we have two measure points i)speed (if any code takes less time to solve any problem means it is efficent on comparison of other porgramm which take more time to solve same paroblem.ii)space(stroge) the programm which takes less space in our memory is more efficient)}
# How to measure time taken by a code to run
# import time
# start=time.time() #strting time
# i=1
# while(i<101):
#   print(i)
#   i+=1
# # for i in range(1,101):
#   # print(i)

# print(time.time()-start)#here time.time()-->current time--->output=0.020s in case of for loop but in case of while it is 0.022  ***********But again it is not a correct method to measure time efficiency since this method is based on system configration means in diffrent machine the time will be diffrent since diffrent machine have diffrent speed due to theri configration and also this is also a problem that on small change just like here we changes for loop into while loop but our logic is same but we will get diffrent time 
# WE HAVE TARGET TO FIND A RELATION BETWEEN TIME AND INPUT 
# 2.method for measuring efficieny is couting operation(steps) involved in a Programm {Remember that return statment inside a funcion is not an operation or step isko count kare ya na kare ye ek problem hai is stepCount method ka}  
# 3.METHOD (ORDER OF GROWTH--->and also it is the best way to find a relation between time and input and it is not neccesary that the relation between time and input should be exact means if it is n^2+n then if we say that the relation between time and input is quadratic then also (HAMRA KAM CHALEGA))   {************Remember that whenever we are designing an algorithm we must consider the worst case always also {n^2 means nested loop} and {only n means simple loop} so during finding the relation between time and input we will consider that factor that will take more time}
# we have a method for finding order of growth it is called Big Oh or O() method
# L=[1,2,3,4,5]
# for i in L:
#   for j in L:
#    print([i,j])  


# print("Hello sir I am Ravi Prajapati")
# first method to write this  prograam for multiply two numbers using *
# def multipy(a=2,b=4):
#   return a*b
# second method to write this  prograam for multiply two numbers using loop

# def multipy(a=2,b=4):
#   result=0
#   for i in range(b):
#     result= result+a
#   return result
      
# print(multipy(3,4))


# print(multipy(2,4))
# third method to write this  prograam for multiply two numbers using recursion (for this remember that all work which can be done by loop can also be done using recursion)
# def multiply(a,b):
#   if(b==1):
#     return a
#   else:
#     return a+multiply(a,b-1)
# print(multiply(2,3))
# finding factorial of a number using recursion
# def fact(n):
#   if(n==1):
#    return n
#   else:
#     return n*fact(n-1)
  
# # print(mystr.index('q'))
# print(fact(5))
# write a function to check that if a given string is palindrome or not using recursion
# here our base case will be that if a string has only one char then it will be a plalindrome itself
# def Palidrome(word):
#   if(len(word)==0 or word==''):
#     return "Palindrome"
#   else:
#     if(word[(len(word)-1)]==word[0]):
#       # return (word[1:len(word)-1])
#       return Palidrome(word[1:len(word)-1])
#     else:
#       return "Not Palindrome"
# print(Palidrome("maam"))

# Function to find fabonacci value at any index (FIRST METHOD GHATIYA METHOD) This method is ghatiya since it calculates all the values every time and dueto this it takes much more time which make it inefficient
# def fib(n):
#   if(n==0 or n==1):
#     return 1
#   else:
#     return fib(n-1)+fib(n-2)
  
# print(fib(5))
# Function to find fabonacci value at any index (SECOND METHOD MASTA METHOD using memoization method)
# dic={0:1,1:1}
# # print(dic[0])
# def fib(n,dic):
#   if(n in dic):
#     return dic[n]
#   else:
#      dic[n]=fib(n-1,dic)+fib(n-2,dic)
#      return dic[n]


# print(fib(4,dic))
# print(dic)


#<--------------------------------------------  OOPS IN PYTHON FROM APNA COLLEGE------------------------------------------------------>
# class Student:
#   name="Ravi Prajapati"

# # making an object
# s1=Student()
# print(s1.name)

# print(s1)
  
# class Car:
#   name="madhindra"
#   start="yes"
#   stop="yes"
#   id="87878"

# c1=Car()
# print(f"{c1.name} and {c1.start} and {c1.id}")  
# class Student:
#   def __init__(self,name):#this self argument is basically talking about the object and remember first argument of the constructor only will be self
#     print(f"New object is created with name {name}")
#   name="Ravi"
#   SurName="Prajapati"


# s1=Student("Rabba")
# print(s1.name)
# s2=Student("Rama")
# print(s2.name)

# CLASS AND OBJCT ATTRIBUTES
# class Student:
#   College_name="Devi Dayal Hindi Hight School"
#   def __init__(self,name,SurName,Class):
#     self.name=name
#     self.SurName=SurName
#     self.Class=Class

# # MAKING OBJECT OF THIS CLASS
# s1=Student('Rabba','Prajapati',12)
# print(f"The name of the student is {s1.name} and surname is {s1.SurName} and studing in {s1.Class} in college {s1.College_name}")
# class Student:

#   def __init__(self,name,Math,Hindi,Science):
#     self.name=name
#     self.Math=Math
#     self.Hindi=Hindi
#     self.Science=Science
#     print(f"The name of student is {name} and markses of Math Hindi and Science are {Math} {Hindi} {Science}")
#   def avg(self):
#     # print(f"avg of marks is ({Math}+{Hindi}+{Science}) ")
#     print((self.Math+self.Hindi+self.Science)/3)
#   @staticmethod
#   def static():
#     print("static method creating")

 





# s1=Student("Rama",90,89,67)
# print(s1.avg())
# s1.static()
# CRATING A CLASS WITH NAME ACCOUNT  WHICH TAKES TWO ARGUMENTS BALANCE AND ACCOUNTNO AND CREATE TWO METHODS FOR DEBIT AND CREDIT
# class Account:
#   def __init__(self,balance,accountNo):
#     self.balance=balance
#     self.accountNo=accountNo
#     print(f"The Account having AccountNo {accountNo} hava total balance of {balance}")
#     # debit
#   def Debit(self,ammount):
#     self.balance=self.balance-ammount
#     print(f"Your account is debit and total ammount is {self.balance}")
    
#   def Credit(self,ammount):
#     self.balance=self.balance+ammount
#     print(f"Your account is credited and total ammount is {self.balance}")
    
    

# A1=Account(45555,'Asdc')
# A1.Debit(455)
# class Account:
#   def __init__(self,AN,AP):
#     # here in this case AN and AP both are public  component
#     self.AN=AN
#     self.AP=AP

# A1=Account("Rama","Ravi1234")
# print(A1.AN)
# print(A1.AP)
# class Account:
#   def __init__(self,AN,AP):
#     # here in this case AN and AP both are Private  component
#     self._AN=AN
#     self._AP=AP

# A1=Account("Rama","Ravi1234")
# print(A1.AN)
# print(A1.AP)
    

# A1=Account("Rama","Ravi1234")
# print(A1.AN)
# print(A1.AP)
# class Account:
#   def __init__(self,AN,AP):
    
#     self.AN=AN
#     self.AP=AP
#   @staticmethod  
#   def _Greet():#now this function also is a private component
#    print("Hello sir")
# A1=Account("Rama","Ravi1234")
# print(A1.AN)
# print(A1.AP)
# A1.__Greet()
#<---------------------------------------- WE CAN NOT USE ALL THIS PRIVATE FUNCTIONS AND ATTRIBUTES OUTSIDE AN CLASS SO THEY ARE  USED INSIDE THE CLASS BUT INSIDE ANY OTHER FUNCTION OR ATTRIBUTES--------------------------------------------------------->
# class Account:
#   @staticmethod
#   def __Greet():
#     print("Hello sir Jj")
  
  
#   def Greet2(self):
#     self.__Greet()
#     print("Hello Good AfterNoon sir ji")


# A1=Account()
# A1.Greet2()
# A1.__Greet()
# class Car:#Parent Class
#   @staticmethod
#   def start():
#     print("car started")
    
#   @staticmethod
#   def stop():
#     print("car stopped")
# <-----------LEVEL1--------------------->
# class MahindraCar(Car):#Child class
#   @staticmethod
#   def acce():
#     print("accelerate my car")
#   @staticmethod
#   def Dance():
#     print("Dance my car")
# <-----------LEVEL2--------------------->


# class BoleroCar(MahindraCar):
#   @staticmethod
#   def Bolero():
#       print("This is  my Bolero car")


# c1=BoleroCar()
# c1.acce()
# c1.start()
# c1.stop()
# c1.Dance()
# c1.Bolero()
# <------------MULTIPLE INHERITANCE----------------------------->
# class A:
#   @staticmethod
#   def Hello():
#     print("Hello  sir How are you?")
# class C:
#   @staticmethod
#   def Hello2():
#     print("Hello2  sir How are you?")
# class B:
#   @staticmethod
#   def Hello1():
#     print("Hello1  sir How are you?")
# class D:
#   @staticmethod
#   def Hello3():
#     print("Hello4  sir How are you?")
# class E:
#   @staticmethod
#   def Hello4():
#     print("Hello  sir How are you?")

#     # NOW MAKINGA CHILD CLASS WHICH INCLUDES ALL THE METHODS OF ALL THE CLASS A,B,C,D,E
# class Child(A,B,C,D,E):
#   @staticmethod
#   def child():
#     print("Hello  I am child class How are you?")
# c1=Child()
# c1.child()
# c1.Hello()
# c1.Hello1()
# c1.Hello2()
# class Car:
#   def __init__(self,type):
#     # self.name=name
    
#     self.type=type

# class f,name,type):
#     self.name=name
#     super().__init__(type)

    
# A1=Mahindra("MahindraMahindra(Car):
#   def __init__(sel","Electric")
# print(A1.name)
# print(A1.type)
# here actually person class have a it's own name variable and inside the constructor the name which is used is only for objects
# <--------------First secnerio------------------->
# class Person:
#   name="Pata Nahi"
#   def __init__(self,name):
#     self.name=name #self.name means a new variable it is not talking about name='Pata Nahi'
    



# p1=Person("Ram")
# print(Person.name)#------->Pata Nahi
# print(p1.name)#---------->Ram
# <--------------second secnerio------------------->
# class Person:
#   name="Pata Nahi"
#   def __init__(self,name):
#     Person.name=name
    



# p1=Person("Ram")
# print(Person.name)#------>Ram
# print(p1.name)#------------>Ram
# <--------------Third secnerio------------------->
# class Person:
#   name="Pata Nahi"
#   def __init__(self,name):
#     self.__class__.name=name

#     p1=Person("Ram")
#     print(Person.name)#------>Ram
#     print(p1.name)#------------>Ram


# <--------------Fourth secnerio usng class method------------------->
# class Person:
#   name="Pata Nahi"
#   @classmethod
#   def ChangeName(cls,name):
#     cls.name=name

# p1=Person()
# # p1.ChangeName("rama")
# # print(p1.name)#-->rama
# # print(Person.name)#-->rama

# print(p1.name)#-->Pata Nahi
# p1.ChangeName("rama")
# print(Person.name)#-->rama
# <---------------UNDERSTANDING @property method---------------------->
# class Person:
#   def __init__(self,name,Math,Hindi,Phy):
#     self.name=name
#     self.Math=Math
#     self.Hindi=Hindi
#     self.Phy=Phy
#     # now if we want to find Avg of all these marks
#   def Avg(self):
#     self.Avg=(self.Math+self.Hindi+self.Phy)/3





# p1=Person("Rama",34,56,78)
# print(p1.Avg)
# p1.Phy=89
# print(p1.Phy)
# p1.Avg()
# print(p1.Avg)
# <---------------------------------------------------------->
# class Person:
#   def __init__(self,name,Math,Hindi,Phy):
#     self.name=name
#     self.Math=Math
#     self.Hindi=Hindi
#     self.Phy=Phy
#     # now if we want to find Avg of all these marks
#   @property
#   def Avg(self):
#    return (self.Math+self.Hindi+self.Phy)/3





# p1=Person("Rama",34,56,78)
# print(p1.Avg)
# p1.Phy=89
# print(p1.Phy)
# p1.Avg()
# print(p1.Avg)      


# print("Hello I am Ravi Prajapati")
# METHOD1
# class Complex:
#   def __init__(self,real,img):
#     self.real=real
#     self.img=img
#   def ShowNumber(self):
#     print(f"{self.real}+{self.img}i")
#   def Add(self,num2):
#     newreal=self.real+num2.real
#     newimg=self.img+num2.img
#     return Complex(newreal,newimg)
# num1=Complex(12,34)
# num2=Complex(12,34)
# num1.Add(num2).ShowNumber()
# METHOD2
# class Complex:
#   def __init__(self,real,img):
#     self.real=real
#     self.img=img
#   def ShowNumber(self):
#     print(f"{self.real}+{self.img}i")
#   def __add__(self,num2):
#     newreal=self.real+num2.real
#     newimg=self.img+num2.img
#     return Complex(newreal,newimg)
# num1=Complex(12,34)
# num2=Complex(12,34)
# # num1.Add(num2).ShowNumber()
# # print(num1+num2)
# num3=num1+num2
# num3.ShowNumber()
# # num1.ShowNumber()
#<------------NOW MAKING OUR OWN CLASS WHICH ACT SAME AS LIST CLASS IN PYTHON-------------------->
# print("Hello I am Ravi Prajapati and i am studing in class12 and learning python from apna college")
# import ctypes
# class List:
#   def __init__(self):
#     self.size=1#-->total size of the list
#     self.n=0#-->total elements present in the list
#     self.A=self.CreateArray(self.size)        


#   def CreateArray(self,capacity):
# # creating an array with size =self.size(capacity) and also it will be a refrential array
#     return (capacity*ctypes.py_object)()
# #   # now making a function for showing length of the list on len(listname) for this we use a magic method
#   def __len__(self):
#     return self.n
#   # now making a function for append any element in the list
#   def append(self,element):
#     if(self.n==self.size):#->their is no space for add element in the list so 1.we have to create a new array having size double of previous
#       B=self.CreateArray(self.size*2)
#       self.size*=2
# #       # 2.now we have to copy all the elements of the previous array
#       for i in range(self.n):
#         B[i]=self.A[i]
# #       # 3.also we have to add the new element for which we did this all process
#       B[self.n]=element
#       self.n+=1
#       self.A=B
#     else:
# #       # already space is present so we have to only add the new elements inside this array
#       self.A[self.n]=element
#       self.n+=1
# # # Now adding print functionality so that on doing print(listname) we can print our list for this we will use str magic method
#   def __str__(self):
#     result=''
#     for i in range(self.n):
       
#        result=result+str(self.A[i])+','

#     return (f"[{result[:-1]}]")
# # # Now adding indexing feature means listname[0] then we will get value at 0 index
#   def __getitem__(self,index):
#     if(index>=0 and index<=self.n):
#       return self.A[index]
#     else:
#       return []
# # Now adding pop() functinailty
#   def pop(self):
    
#     if(self.n==0):
#       return 'Empty list'
    
#     else:
#       self.n-=1
#       return self.A[self.n]
        
# # Now adding functionality for clear
#   def clear(self):
#     self.A=[]
#     self.n=0
#     self.size=1
    
# # # Now adding functionality for find index(listelement) it return the index if the element is present else throw error
#   def find(self,item):
#     for i in range(self.n):
#       if(item==(self.A[i])):
#         return i
#       else:
#         return "This element does not exist in this list"
# # # Now adding functionality for insert an element at any index
#   def insert(self,idx,item):
#     if(self.n==self.size):#space nahi hai
#       #1.create a new array
#       C=self.CreateArray(self.size*2)
#       #2.copying all the data of the previous array in this new array
#       self.size*=2
#       for i in range(self.n):
#         C[i]=self.A[i]
#       for i in range(self.n,idx,-1):
#         C[i]=C[i-1]
#       C[idx]=item
#       self.n+=1
#       self.A=C


#     else:
#       for i in range(self.n,idx,-1):
#         self.A[i]=self.A[i-1]
#       self.A[idx]=item
#       self.n+=1
      
      
# #     # Adding functinality for delete an element at any index for this we use a magic function __delitem__(self,idx)
#   def __delitem__(self,idx):
#     # Delete bhi lafda wali cheez hai kaise dekhte hai-->
#     # for delete first we have to remove this item from list and then we have to shift all remaining elements having index greater then the index of deleted element and also self.n-=1
#     if(idx>=0 and idx<self.n):
#       for i in range(idx,self.n-1):
#         self.A[i]=self.A[i+1]
#       self.n-=1
#     else:
#        print("item does not exist in this list")
#       #  self.A[idx]

      
#   def remove(self,item):
#     for i in range(self.n):
#           if(i>=0 and i<self.n and self.A[i]==item):
#             for i in range(i,self.n-1):
#               self.A[i]=self.A[i+1]
#             self.n-=1
            
      
    
# l1=List()
# l1.append(2)
# l1.append('hello')
# l1.append('hello1')
# print(l1)
# del l1[100]
# l1.remove('hello1')
# l1.insert(2,'Rabba')
# print(l1)
# print(l1.find(29))
# l1.pop()
# l1.pop()
# l1.pop()
# print(l1)
# print(l1[1])
# # l1.insert(2,'jiji')
# # del l1[900]
# l1.remove(3)
# print(l1)
# print(l1.find(5))

# <------------------CREATING A LINKED LIST---------------------------------> 
# for creating a linked list first of all we have to create a class for Node since a Linked List is collection of Nodes

class Node:
  def __init__(self,value):
    # initially the node we will creating have data as value provided and in their address section we initially store None
    self.data=value
    self.next=None
# Now since LinkedList is collection of Nodes hence using above Node we will make our LinkedList class
class LinkedList:
  def __init__(self):
    # initially we will create an empty LL means it have zero Node(element) inside it
    # This is condition of an empty LL
    self.head=None  #remember that self.head means a complete Node
    self.n=0  #-->it tail the total no of nodes present in the LL
  def __len__(self):
    return self.n
  def InsertFromHead(self,item):
      new_node=Node(item)
      new_node.next=self.head  #so here our whole curr node is the address hence complete node is stored in the next of new_node
      self.head=new_node
      self.n+=1
  def __str__(self):
    curr=self.head
    result=''
    while(curr!=None):
      result+=str(curr.data)+'->'
      curr=curr.next  
    return result[:-2]
  def append(self,item):
    if(self.head!=None): #means LL is not empty
      curr=self.head
      new_node=Node(item)
      while(curr.next!=None):
          curr=curr.next
      curr.next=new_node
      # new_node.next=None
      self.n+=1
    if(self.head==None):#means LL is empty
      self.InsertFromHead(item)
# Now insert after a given element
  def InsertAfter(self,after,item):

    new_node=Node(item)
    curr=self.head
    while(curr!=None):
      if(curr.data==after):
         new_node.next=curr.next
         curr.next=new_node
         self.n+=1
         break
      curr=curr.next
    if(curr==None):#matlab loop completely chala hai 
      print("Item Not found")


  def clear(self):
    self.head=None
    self.n=0
  def DeleteFromHead(self):
    # curr=self.head
    if(self.head!=None):
      self.head=self.head.next
      self.n-=1
    if(self.head==None):
      print("Empty LL",end='')
  def pop(self):
    
    curr=self.head
    if(self.n==1):
      # print("1")
      return self.DeleteFromHead()
    elif(self.n==0):
      return 'empty LL'  
    else:
      while(curr.next.next!=None):
        curr=curr.next
      curr.next=None
      self.n-=1  
  def remove(self,item):
    curr=self.head
    if(self.n==1 or self.head.data==item):
      self.DeleteFromHead()
      # print('1')
    elif(self.head==None and self.n==0):
      return 'Empty LL'  
    else:  
      while(curr!=None):
        # print(curr.next.data)
        if(curr.next.data==item):
          break
          
        curr=curr.next
      # two cases 
    # 1.item Nahi mila
      if(curr.next==None):
        return 'Item Not found'
      else:
        curr.next=curr.next.next
        self.n-=1
# SEARCH ALGORITHAM
# METHOD 1
  def search(self,item):
    curr=self.head
    index=0
    while(curr!=None):
      if(curr.data==item):
        print(f'item found at index {index}')
      curr=curr.next
      index+=1
    print('Item Not found')  


  def __getitem__(self,index):
    curr=self.head
    pos=0
    while(curr!=None):
       if(index==pos):
         return (f'item is {curr.data}')
       curr=curr.next
       pos+=1
    return 'Item Not found'   
     
    # METHOD 2 (PATHA NAHI KYA PROBLEM HAI)

  # def search(self,item):
  #   curr=self.head
  #   index=0
  #   while(curr!=None):
  #     if(curr.data==item):
  #       break
  #     curr=curr.next
  #     index+=1
  #   if(curr.next==None):
  #     return 'Item Not found'  
  #   else:
  #     return (f"Item found at index {index}")


  
LL=LinkedList()

# NOW CREATING A STACK CLASS USING CONECPT OF LINKED LIST
class Node:
  def __init__(self,value):
    self.data=value
    self.next=None
class Stack:
  def __init__(self):
    # condition for a empty stack---------> in linked list jo kam self.head variable karta tha vahi kam stack me self.top variable karega  if we want then we can take same name of variable
    self.top=None    
  def IsEmpty(self):#it returs true if stack is empty
    return self.top==None
  def push(self,item):
    new_node=Node(item)
    curr=self.top
    new_node.next=curr
    self.top=new_node #reassigning head node
    # self.top=new_node
  def traverse(self):
    curr=self.top
    while(curr!=None):
      print(curr.data,end=' ')
      curr=curr.next
  def peek(self):
    if(self.top==None):
      print("Stack is empty Now")
    else:  
      print(f'element at top is {self.top.data}')
  def pop(self):
    if(self.top==None):
      print("Stack is empty Now")
    else:
      curr=self.top
      # self.top.next=None
      self.top=curr.next
      return curr.data
  def size(self):
    curr=self.top
    index=0
    while(curr!=None):
      curr=curr.next
      index+=1
    # return (f'size of the stack is {index}')
    return index
  
# <-----------------PROGRAMM TO REVERSE A STRING USING STACK-------------------------------------------------->
  def ReverseString(self,str):
  # str='Hello'
    for i in str:
      self.push(i)
    revstr=''
    for i in range(len(str)):
        revstr+=s.pop()
    print(revstr)    
  
  def TextEditor(self,Text,Pattern):
    u=Stack()
    r=Stack()
    for i in Text:
        u.push(i)
    for i in Pattern:
      if(i=='u'):
        data=u.pop()   
        r.push(data)
      if(i=='r'):
        data1=r.pop()
        u.push(data1)
    # print(u.IsEmpty())
    string=''
    while(u.IsEmpty()==False):
      # print("hello")  
      # u.pop()
      string=u.pop()+string
    # u.traverse()  
    print(string)
s1=Stack()
s=Stack()
s.push(1)
s.push(2)
s.push(3)
# print(s)
# s.traverse()
# print(s.size())
# <----------------------CREATING A 2D LIST------------------------------------------->
# L=[
#   [0,0,1,1],
#   [1,0,0,1],
#   [0,1,1,1]
# ]
# # print(L[0])
# for i in L:
#   print(i)






# print(s.IsEmpty())
# s.push("hello")
# s.push("hello1")
# s.push("hello2")
# s.ReverseString('kya be kya kar raha hai shale')
# s1.TextEditor('Ravi Prajapati','uuurrr')

# print(s.IsEmpty())
# print(s.pop())
# s.traverse()
# s.traverse()
# s.pop()
# s.pop()
# s.pop()
# s.traverse()

