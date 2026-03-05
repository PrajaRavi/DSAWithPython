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
      # print("True")
      return True
    else:
      # print("False")
      return False
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


mydic={
  '+':1,
  '-':1,
  '*':2,
  '/':2,
  '^':3,
  # '(':4,
}

def InfixExpressEvaluation(mystr,s1,s2):
    for i in mystr:
      if(i=='+' or i=='-' or i=='*' or i=='/' or i=="("):
        if(s1.IsEmpty):
          s1.push(i)
        else:
          if(i=='('):
            s1.push(i)
          else:  
            if(s1.peek()=="("):
              s1.push(i)
            elif(mydic[s1.peek()]>=mydic[i]):
              if(s1.peek()=="+"):
                s1.pop()
                a=int(s2.pop())
                b=int(s2.pop())
                data=b+a
                s2.push(data)
              elif(s1.peek()=="-"):
                s1.pop()
                a=int(s2.pop())
                b=int(s2.pop())
                data=b-a
                s2.push(data)
              elif(s1.peek()=="*"):
                s1.pop()
                a=int(s2.pop())
                b=int(s2.pop())
                data=b*a
                s2.push(data)
              elif(s1.peek()=="/"):
                s1.pop()
                a=int(s2.pop())
                b=int(s2.pop())
                data=b/a
                s2.push(data)
            else:
              s1.push(i)    
      elif(i==')'):
        while(s1.peek()!="("):
          if(s1.peek()=="+"):
                s1.pop()
                a=int(s2.pop())
                b=int(s2.pop())
                data=b+a
                s2.push(data)
          elif(s1.peek()=="-"):
                s1.pop()
                a=int(s2.pop())
                b=int(s2.pop())
                data=b-a
                s2.push(data)
          elif(s1.peek()=="*"):
                s1.pop()
                a=int(s2.pop())
                b=int(s2.pop())
                data=b*a
                s2.push(data)
          elif(s1.peek()=="/"):
                s1.pop()
                a=int(s2.pop())
                b=int(s2.pop())
                data=b/a
                s2.push(data)

        s1.pop()        

          
      else:
        s2.push(i)
    while(s1.size()>0):
            if(s1.peek()=="+"):
              s1.pop()
              a=int(s2.pop())
              b=int(s2.pop())
              data=b+a
              s2.push(data)
            elif(s1.peek()=="-"):
              s1.pop()
              a=int(s2.pop())
              b=int(s2.pop())
              data=b-a
              s2.push(data)
            elif(s1.peek()=="*"):
              s1.pop()
              a=int(s2.pop())
              b=int(s2.pop())
              data=b*a
              s2.push(data)
            elif(s1.peek()=="/"):
              s1.pop()
              a=int(s2.pop())
              b=int(s2.pop())
              data=b/a
              s2.push(data)
    print(s2.pop())          

def ApplyOperationForPrefix(s2,op):
   b=s2.pop()
   a=s2.pop()   
   data=f"{op}{a}{b}"
   s2.push(data)
   return s2

def ApplyOperationForPostfix(s2,op):
   b=s2.pop()
   a=s2.pop()   
   data=f"{a}{b}{op}"
   s2.push(data)
   return s2


              
def InfixToPrefix(mystr,s1,s2):
    for i in mystr:
      if(i=='+' or i=='-' or i=='*' or i=='/' or i=="("):
        if(s1.IsEmpty()):
          s1.push(i)
        else:
          if(i=='('):
            s1.push(i)
          else:  
            if(s1.peek()=="("):
              s1.push(i)
            elif(mydic[s1.peek()]>=mydic[i]):
              if(s1.peek()=="+"):
                s1.pop()
                s2=ApplyOperationForPrefix(s2,'+')
              elif(s1.peek()=="-"):
                s1.pop()
                s2=ApplyOperationForPrefix(s2,'-')
              elif(s1.peek()=="*"):
                s1.pop()
                s2=ApplyOperationForPrefix(s2,'*')
              elif(s1.peek()=="/"):
                s1.pop()
                s2=ApplyOperationForPrefix(s2,'/')
            else:
              s1.push(i)    
      elif(i==')'):
        while(s1.peek()!="("):
          if(s1.peek()=="+"):
                s1.pop()
                s2=ApplyOperationForPrefix(s2,'+')

          elif(s1.peek()=="-"):
                s1.pop()
                s2=ApplyOperationForPrefix(s2,'-')
          elif(s1.peek()=="*"):
                s1.pop()
                s2=ApplyOperationForPrefix(s2,'*')
          elif(s1.peek()=="/"):
                s1.pop()
                s2=ApplyOperationForPrefix(s2,'/')
        s1.pop()        
      else:
        s2.push(i)
    while(s1.size()>0):
            if(s1.peek()=="+"):
              s1.pop()
              s2=ApplyOperationForPrefix(s2,'+')
            elif(s1.peek()=="-"):
              s1.pop()
              s2=ApplyOperationForPrefix(s2,'-')
            elif(s1.peek()=="*"):
              s1.pop()
              s2=ApplyOperationForPrefix(s2,'*')
            elif(s1.peek()=="/"):
              s1.pop()
              s2=ApplyOperationForPrefix(s2,'/')
    print(s2.pop())  

def InfixToPostfix(mystr,s1,s2):
    for i in mystr:
      if(i=='+' or i=='-' or i=='*' or i=='/' or i=="("):
        if(s1.IsEmpty()):
          s1.push(i)
        else:
          if(i=='('):
            s1.push(i)
          else:  
            if(s1.peek()=="("):
              s1.push(i)
            elif(mydic[s1.peek()]>=mydic[i]):
              if(s1.peek()=="+"):
                s1.pop()
                s2=ApplyOperationForPostfix(s2,'+')
              elif(s1.peek()=="-"):
                s1.pop()
                s2=ApplyOperationForPostfix(s2,'-')
              elif(s1.peek()=="*"):
                s1.pop()
                s2=ApplyOperationForPostfix(s2,'*')
              elif(s1.peek()=="/"):
                s1.pop()
                s2=ApplyOperationForPostfix(s2,'/')
            else:
              s1.push(i)    
      elif(i==')'):
        while(s1.peek()!="("):
          if(s1.peek()=="+"):
                s1.pop()
                s2=ApplyOperationForPostfix(s2,'+')

          elif(s1.peek()=="-"):
                s1.pop()
                s2=ApplyOperationForPostfix(s2,'-')
          elif(s1.peek()=="*"):
                s1.pop()
                s2=ApplyOperationForPostfix(s2,'*')
          elif(s1.peek()=="/"):
                s1.pop()
                s2=ApplyOperationForPostfix(s2,'/')
        s1.pop()        
      else:
        s2.push(i)
    while(s1.size()>0):
            if(s1.peek()=="+"):
              s1.pop()
              s2=ApplyOperationForPostfix(s2,'+')
            elif(s1.peek()=="-"):
              s1.pop()
              s2=ApplyOperationForPostfix(s2,'-')
            elif(s1.peek()=="*"):
              s1.pop()
              s2=ApplyOperationForPostfix(s2,'*')
            elif(s1.peek()=="/"):
              s1.pop()
              s2=ApplyOperationForPostfix(s2,'/')
    print(s2.pop())          

def PostfixEvaluation(mystr,s1):
   for i in mystr:
      if(i=='-'or i=='+' or i=='*' or i=='/'):
        if(not s1.IsEmpty()):        
            b=s1.pop()
            a=s1.pop()
            if(i=='+'):
               data=int(a)+int(b)
               s1.push(data)
            elif(i=='-'):   
               data=int(a)-int(b)
               s1.push(data)
            elif(i=='*'):   
               data=int(a)*int(b)
               s1.push(data)
            elif(i=='/'):   
               data=int(a)/int(b)
               s1.push(data)
      else:
         s1.push(i)   
   print(s1.pop())    

def PrefixEvaluation(mystr,s1):
  # in Postfix evaluation we move from 0th index to the last index of the string but in Prefix we move from last index to 0th index
  pass 
def PrefixToPostfix(mystr,s1):
   for i in mystr[::-1]:
    if(i=='-'or i=='+' or i=='*' or i=='/'):
        if(not s1.IsEmpty()):        
            a=s1.pop()
            b=s1.pop()
            if(i=='+'):
               data=f"{a}{b}+"
               s1.push(data)
            elif(i=='-'):   
               data=f"{a}{b}-"
               s1.push(data)
            elif(i=='*'):   
               data=f"{a}{b}*"
               s1.push(data)
            elif(i=='/'):   
               data=f"{a}{b}/"
               s1.push(data)
    else:
         s1.push(i)   
   print(s1.pop())   

def PostfixToPrefix(mystr,s1):
   for i in mystr:
    if(i=='-'or i=='+' or i=='*' or i=='/'):
        if(not s1.IsEmpty()):        
            b=s1.pop()
            a=s1.pop()
            if(i=='+'):
               data=f"+{a}{b}"
               s1.push(data)
            elif(i=='-'):   
               data=f"-{a}{b}"
               s1.push(data)
            elif(i=='*'):   
               data=f"*{a}{b}"
               s1.push(data)
            elif(i=='/'):   
               data=f"/{a}{b}"
               s1.push(data)
    else:
         s1.push(i)   
   print(s1.pop())   

def PostfixToInfix(mystr,s1):
   for i in mystr:
    if(i=='-'or i=='+' or i=='*' or i=='/'):
        if(not s1.IsEmpty()):        
            b=s1.pop()
            a=s1.pop()
            if(i=='+'):
               data=f"{a}+{b}"
               s1.push(data)
            elif(i=='-'):   
               data=f"{a}-{b}"
               s1.push(data)
            elif(i=='*'):   
               data=f"{a}*{b}"
               s1.push(data)
            elif(i=='/'):   
               data=f"{a}/{b}"
               s1.push(data)
    else:
         s1.push(i)   
   print(s1.pop())



   
s1=Stack()
s2=Stack()
# PrefixToPostfix("-9/*+5346",s1)
# PostfixToPrefix("953+4*6/-",s1)
PostfixToInfix("953+4*6/-",s1)
# PostfixEvaluation("953+4*6/-",s1)                


                


                
                

                

              


              
              
              
   
