# magic method=>dunder functions(method)=>special functions all the method stat with __ and end with __ main point is that all magic methods can't be called by object they will call itself when any object is created. self means the object itself
# instance variable-> variables having diffrent values for diffrent objects
# class/static variable-> variable having same value for diffrent objects
# also instance variables are inside constructor and class variables are outside constructor


# class ATM:
# # static/class variable
#   __counter=0
#   # instance variables
#   def SetCounter(self,value):
#     if type(value)==int:
#       self.__counter==value
#     else:
#       print("cant do this operation") 

#   def __init__(self):
#     # print(id(self))
#     self.sno=ATM.__counter #class variables are called using class_name.variable_name and to make them private use 
#     # __static_variable_name
#     ATM.__counter+=1
#     self.__a=''
#     self.__pin=''
#     self.__balance=0
#     while(self.__a!='5'):
#       self.__a=input('''
# How would you like to proceed???
# 1.Enter 1 to create pin-->
# 2.Enter 2 for debit-->
# 3.Enter 3 for credit-->
# 4.Enter 4 for check balance-->
# 5.Enter 5 for exit -->
                   
# ''')  
#       if(self.__a=='1'):
#         pin=input("Enter 4 digit pin--> ")
#         if(len(pin)==4 and type(pin)==str):
#           self.__pin=pin
#         else:
#           print("pin should have 4 digit")
      
#       elif(self.__a=='2'):
#         if(self.__pin):        
#           self.temp=input("Enter 4 digit pin--> ")
#           if(int(self.temp)==int(self.__pin)):
#             self.__amount=input("Enter Amount--> ")
#             self.__balance=self.__balance+int(self.__amount)
#             print("operation successfully")
#           else:
#             print("Invalid pin")
#         else:
#           print('first create pin')   
#       elif(self.__a=='3'):
#         self.temp=input("Enter 4 digit pin--> ")
#         if(int(self.temp)==int(self.__pin)):
#           self.__amount=input("Enter Amount--> ")
#           if(int(self.__amount)<int(self.__balance)):
#             self.__balance=self.__balance-int(self.__amount)
#             print("operation successfully")
#           else:
#             print("Your balance is less")  
#         else:
#           print("Invalid pin")
      
#       elif(self.__a=='4'):
#         print(f"Your balance is {self.__balance}")
        
#       elif(self.__a=='5'):
#         print("Bye Have a good day!!!")
       

# b=ATM()
# b1=ATM()
# b1.SetCounter(23)
# print(id(b))
# All magic methods
# 1.constructor
# 2.__str__-->it will called when ever we use print() method
# 3.__add__-->method
# 4.__sub__
# 5.__mul__
# Instance variable->are variables which have diffrent value for diffrent objects
# To make any variable private use __ just before it
# What happen when we decalare any variale as private then in backend when interpreter see this __variable_name then it convert this variable into _className__variable_name due to this reson after declaring private to any variable we can't access it outside class so overall
# In python nothin is truly private
# so we should also create a setter and a getter function for each private variables 
# refrence variable
# when we creating variable_name=class_name()-->here variable_name is not a object but it is basically a refrence of that class 
# An important thing that object instance create of a class is mutalbe means we can update it without chaging it's locations so overall objects of class is mutable just like list,dictionary and sets

#<---------------------------appending some element to tuple--------------------------->
# mytup=(1,2,3)
# newtup=mytup+(4,5,6)
# print(newtup)

# fraction class
# class Fraction:
  
#   __deno=0
#   __num=0
#   def __init__(self,__num,__deno):
#     if(type(__deno)==int and type(__num)==int):

#       self.__deno=__deno
#       self.__num=__num
#       # print(f"{self.__num}/{self.__deno}")
#     else: print("Cant create please provide an integer")
  
#   def __str__(self):
#     return (f"{self.__num}/{self.__deno}")
#   def __sub__(self,other):
#     if(self.__num*other.__deno>self.__deno*other.__num):
#       temp___num=self.__num*other.__deno-self.__deno*other.__num
#       temp___deno=self.__deno*other.__deno
#     else:
#       temp___num=self.__deno*other.__num-self.__num*other.__deno
#       temp___deno=self.__deno*other.__deno

#     return (f"{temp___num}/{temp___deno}")
#   def __mul__(self,other):
#     temp___num=self.__num*other.__num
#     temp___deno=self.__deno*other.__deno
#     return (f"{temp___num}/{temp___deno}")
#   def __truediv__(self,other):
#     temp___num=self.__num*other.__deno
#     temp___deno=self.__deno*other.__num
#     return (f"{temp___num}/{temp___deno}")
#   def __add__(self,other): #here self will contain the first parameter and other will contain second parameter
#     temp___num=self.__num*other.__deno+self.__deno*other.__num
#     temp___deno=self.__deno*other.__deno
#     return (f"{temp___num}/{temp___deno}")

# f1=Fraction(2,34)
# print(f1)
# f2=Fraction(2,2)
# print(f1+f2)
# print(f1-f2)
# print(f1*f2)
# print(f1/f2)

# class Customer:
#   def __init__(self,name,gender):
#     self.__name=name
#     self.__gender=gender
#   def Greet(self,obj):
#     if(obj.__gender=="Male" or obj.__gender=="male" ):
#       # obj.name="Hello I am Ravi prajapti"
#       print(f"Good morning {obj.__name} Sir")
#     else:  
#       # obj.name="Hello I am Ravi prajapti"
#       print(f"Good morning {obj.__name} Mam")
# c1=Customer("Ravi Prajapati","Male")
# c1.Greet(c1) #-->it is by default call by refrence
# print(c1.name)

# Relation between classes
# 1.Aggregation(Has a relationship) 2.Inheritance(is a relationship)
# example of inharitance
# i)a smartphone {is a} product
# ii)a car {is a} vehichle
# example of Aggregations
# i)Customer {has a} address(customer(class)<>(diamond shape)----Address(class))

# Example of Aggregations
# class Customer:
#   def __init__(self,name,address,gender):
#     self.name=name
#     self.address=address
#     self.gender=gender
#   def EditProfile(self,new_name,new_gender,new_city,new_pin,new_state):
#     self.name=new_name
#     # self.address=new_add
#     self.address.ChangeAdd(new_city,new_pin,new_state)
#     self.gender=new_gender
# class Address:
#   def __init__(self,city,pincode,state):
#     self.city=city
#     self.pincode=pincode
#     self.state=state
#   def ChangeAdd(self,new_City,new_pin,new_state):
#     self.city=new_City
#     self.pincode=new_pin
#     self.state=new_state  
# add=Address("kalyan",421306,"Maharashtra")

# c1=Customer("Ravi",add,"Male")
# c1.EditProfile("Pranshu","Female","Saraimeer",27635,"UtterPradesh")
# print(c1.name)
# print(c1.address.state)

#Example of Inheritance 
# If we didn't created any constructor in child class then bydefault the object of child class call parents constructor
# Polymorphism
# i)Method overriding(means child class method will override on parent class method )
# ii)Method overloading(a function having same name but it can do diffrent task)
# iii)Operator overloading(same operator using for diffrent task)

class Person:
 def Greet():
   print("greet from person")
class Monkey:
 def Greet():
   print("greet from monkey")
  

class Ravi(Person,Monkey):
 pass
r=Ravi()
r.Greet() #now above in both the class theri is same Greet() function but remember the greet function is called which is inside first parent(Person) this concept is called MRO(Method Resolution order)
# 70
# good question at the last of the video
























  









