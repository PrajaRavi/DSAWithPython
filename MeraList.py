import ctypes
class MeraList:
  __noprint=-1 #This is the index, the number which is removed using remove function
  __nforremove=0 # i am using this to give a true length after remove function
  __flagforRemove=False #i am adding this so that on the basis of this flag i can repy that the given element during remove is prasent or not
  __flag1=False #i am using this flag so that if a person give wrong index during insert then i can throw an error
  def __init__(self):
    self.__size=1 
    self.__n=0 #totl no of element
    self.__Arr=self.__CreateArray(self.__size)
  def __CreateArray(self,capacity):
# creating an array with size =self.__size(capacity) and also it will be a refrential array
    return (capacity*ctypes.py_object)()
  
  def append(self,value):

      if(self.__n==self.__size):
        # print("if")
        NewArr=self.__CreateArray(self.__size*2)
        self.__size*=2
        for i in range(0,self.__n):
          NewArr[i]=self.__Arr[i]
        NewArr[self.__n]=value
        self.__Arr=NewArr
        self.__n+=1
      else:
          self.__Arr[self.__n]=value
          self.__n+=1     

  def __len__(self):
    return self.__n-self.__nforremove
  def pop(self):
    if(self.__n!=0):
      self.__n-=1  
      return self.__Arr[self.__n]
    else:
      print("You can't pop more")  
  def __getitem__(self,index):
    return self.__Arr[index]
  def clear(self):
    self.__n=0
    self.__size=1
    print(self)
  def __str__(self):
    # print(self.__n)
    mystr=''
    for i in range(0,self.__n):
      # print(self.__Arr[i])
        # print(self.__Arr[i])
        if(i!=self.__noprint):
          mystr+=(f"{self.__Arr[i]},")
    return (f"[{mystr}]")
  def copy(self):
    new_list=MeraList()
    for i in range(0,self.__n):
      new_list.append(self.__Arr[i])
    return new_list
  def remove(self,value):
    for i in range(0,self.__n):
      if(self.__Arr[i]==value):
        self.__noprint=i
        self.__flagforRemove=True
        self.__nforremove+=1
        break
    if(self.__flagforRemove==False):
      print("Item not found")    
  def insert(self,index,value):
    # print(self.__size)
   if(index<=self.__n):
    if(self.__n==self.__size):
        # print("if")

        NewArr=self.__CreateArray(self.__size*2)
        self.__size*=2
        # first copy all the element of the previous array in the new array
        for i in range(0,self.__n):
          NewArr[i]=self.__Arr[i]
        # Now performing shifting 
        for i in range(index,self.__n):
          NewArr[i+1]=NewArr[i]
        NewArr[index]=value   
        self.__Arr=NewArr
        self.__n+=1
    else:
        # Now performing shifting 
          for i in range(index,self.__n):
            self.__Arr[i+1]=self.__Arr[i]
          self.__Arr[index]=value   
          
          self.__n+=1
   else:
     print("wrong index error")          
  def sort(self):
  #  print(self.__n) #3
  #  print(self.__size) #4
    for i in range(0,self.__n): #0,1,2
      for j in range(i,self.__n-1): #
        if(self.__Arr[j]>self.__Arr[j+1]):
          temp=self.__Arr[j]
          self.__Arr[j]=self.__Arr[j+1]
          self.__Arr[j+1]=temp
  
    # print(self.__Arr[0])
  def __delitem__(self,index):
    for i in range(index,self.__n-1): #0,1,2
      # print(i)
      
      self.__Arr[i]=self.__Arr[i+1]
    self.__n-=1  
  def reverse(self):
    i=0
    j=self.__n-1
    while(i<j):
      temp=self.__Arr[i]
      self.__Arr[i]=self.__Arr[j]
      self.__Arr[j]=temp
      i+=1
      j-=1   
  def count(self,value):
    count=0
    for i in range(0,self.__n):
      if(self.__Arr[i]==value):
        count+=1
    return count
  # in python we can delete anything using del keyword so to add (del list[0])so that we can delete element at specific index we have to use a magic method __delitem__ 

l=MeraList()
l.append(5)
l.append("hello1")
l.append(6)
l.append(0)
print(l)
del l[0]
print(l)







