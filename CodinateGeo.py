# defining class for cordinates
import math

class Cordinate:
  def __init__(self,value1,value2):
    if(type(value1)==int and type(value2)==int ):
      self.x1=value1
      self.x2=value2
    else:
      print("cordinate should be a numbers")  
  def __str__(self):
    return f"({self.x1},{self.x2})"
# x1=a,x2=b
class CG:
  def __init__(self):
    pass
    
    
  # function that calculates distance between two points
  def DistanceBwTwoPoint(self,p1,p2):
    result=math.sqrt(math.pow((int(p1.x1)-int(p2.x1)),2)+math.pow((int(p1.x2)-int(p2.x2)),2))
    print(self.__approximation(result))
    return self.__approximation(result)
  def MidePointOfLine(self,p1,p2):
    a1=(p1.x1+p2.x1)/2
    a2=(p1.x2+p2.x2)/2
    print(f"mid point of this line is :({a1},{a2})")  
  def __approximation(self,num1):
    # print(type(num1))
    num=str(num1)
    str1=(num).split('.')[1]
    if(float(str1[0])>=5):
      return (float((num).split('.')[0])+1)
    else:
      return math.floor(float((num).split('.')[0]))
  def SlopeOfLine(self,p1,p2):
    print(f"slope of line is : {(p1.x2-p2.x2)/(p1.x1-p2.x1)}")  
#implementing the section formula
# here a and b are the points and the c(m1,m2),a(x1,x2),b(x1,x2)
  def SectionFormulaInternal(self,a,b,c):
    x=self.__approximation((c.x1*b.x1+c.x2*a.x1)/(c.x1+c.x2)) 
    y=self.__approximation((c.x1*b.x2+c.x2*a.x2)/(c.x1+c.x2))
    print(f"point is : ({x},{y})") 
  def SectionFormulaExternal(self,a,b,c):
    x=self.__approximation((c.x1*b.x1-c.x2*a.x1)/(c.x1-c.x2)) 
    y=self.__approximation((c.x1*b.x2-c.x2*a.x2)/(c.x1-c.x2))
    print(f"point is : ({x},{y})") 
  def Incenter(self,a,b,c):  
    AandB=self.DistanceBwTwoPoint(a,b)
    BandC=self.DistanceBwTwoPoint(b,c)
    AandC=self.DistanceBwTwoPoint(a,c)
    return f"({self.__approximation((AandB*a.x1+BandC*b.x1+AandC*c.x1)/AandB+BandC+AandC)},{self.__approximation((AandB*a.x2+BandC*b.x2+AandC*c.x2)/AandB+BandC+AandC)})"
  

  def TraiangleCentroid(self,a,b,c):
    return f"({self.__approximation((a.x1+b.x1+c.x1)/(3))},{self.__approximation((a.x2+b.x2+c.x2)/(3))})"
 #function to check if the given three lines are concurent or not
  def ThreePointCollinearOrNot(self,p1,p2,p3):
    d1=(self.DistanceBwTwoPoint(p1,p2))
    # d1=self.__approximation(d1)
    d2=(self.DistanceBwTwoPoint(p2,p3)) 
    # d2=self.__approximation(d2)
    d3=(self.DistanceBwTwoPoint(p1,p3))
    # d3=self.__approximation(d3)
    if(d3==d1+d2):
      print("yes")
    else:
      print("no")  
  
    
  
a=Cordinate(-3,10)
b=Cordinate(6,-8)
d=Cordinate(-1,6)

c=CG()
# c.DistanceBwTwoPoint(a,b)
c.SectionFormula(a,b,d)
# c.CollinearOrNot(a,b,d)
# c.CollinearOrNot(a,b,d)



    