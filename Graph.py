class Graph:
  def __init__(self,vno=0): #->means here we have to tell initially that how many vertex we want 
    self.vartex_count=vno
    self.adj_matrix=[[0]*vno for i in range(vno)]
  def add_edge(self,u,v,weight=1):
    """
    [0c,1c,2c
    [0,0,0,0],->0r
    [0,0,0,0],->1r
    [0,0,0,0] ->2r   
    ]
    so this u is respective row and v is respective columns
    """  
    # first check if these values of u and v are valid or not
    if(0<=u<self.vartex_count and 0<=v<self.vartex_count):
    # the graph we are implementing is not a directed graph means we can go from a->b and also a<-b  hence we are doing this twice
      self.adj_matrix[u][v]=weight
      self.adj_matrix[v][u]=weight

    else:
      print("invalid vertex value") 

  def remove_edge(self,u,v):
    if(0<=u<self.vartex_count and 0<=v<self.vartex_count):
    # the graph we are implementing is not a directed graph means we can go from a->b and also a<-b  hence we are doing this twice
      self.adj_matrix[u][v]=0
      self.adj_matrix[v][u]=0

    else:
      print("invalid vertex value")

  def has_edge(self,u,v):     
    if(0<=u<self.vartex_count and 0<=v<self.vartex_count):
       return self.adj_matrix[u][v]!=0
    else:
      print("invalid vertex value")
  def __str__(self):
    mystr=""
    for i in self.adj_matrix:
      mystr=mystr+str(i)+",\n"
          
    return f"[\n{mystr}]"
  

graph=Graph(3)
graph.add_edge(0,1,14)
graph.add_edge(0,2,34)
print(graph)    

# Traversing a graph
"""
!Traversing a graph have only one issue that one node could not traverse more than one hence we devide the vertices inot two categories 1)visited 2)not visited
we use a boolean array to keep record of the visited nodes
BFS->Breadth first search=>uses a queue data structure for traversal,traversing begin from any node which is called source node   
DFS->Depth first search

"""
