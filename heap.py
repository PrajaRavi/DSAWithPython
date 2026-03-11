"""
 Heap data sturcture
 Heap is a sorting algorithm known as heap sort
 Heap is of two type 1)max heap(default) 2) min heap
 condition for a binary tree to be a heap data sturcture 1)the value of any root node in a subtree should be greater or equal to value of each children (max heap) and min heap(the value of any root node in a subtree should be less or equal to value of each children)
 2)heap must be a complete binary tree means siblings or nothing 
->Representation of heap->we use array means we store values inside an array unlike in tree and we use node and linked list reprsentation

"""
mylist=[40,70,10,90,60,30,50,20,80]
class Heap:
    def __init__(self):
        self.Heap=[]

    def GetIndex(self,data):
        for i in range(len(self.Heap)):
            if(self.Heap[i]==data):
                return i    
            
    def Insert(self,data):   

        if(len(self.Heap)==0):
            self.Heap.append(data)
        else:
            self.Heap.append(data)
            l=0
            h=len(self.Heap)-1
            # print(l,h)
            while(l<=h):
                if(self.Heap[l]<=self.Heap[h]):
                    temp=self.Heap[l]
                    self.Heap[l]=self.Heap[h]
                    self.Heap[h]=temp
                l+=1

    def __str__(self):
        return str(self.Heap)
                
    
            
            
heap=Heap()
heap.Insert(40)
heap.Insert(35)
heap.Insert(38)
heap.Insert(32)
# heap.Insert(33)
heap.Insert(36)
heap.Insert(200)
# heap.Insert(15)
# heap.Insert(20)
print(heap)
# heap.RootDelete()
# print(heap.GetIndex(24))
# print(heap)
