import math
class PriorityQueue:
    def __init__(self):
        self.heap=[]
    
    def size(self):
        return len(self.heap)

    def isEmpty(self):
        return self.size() == 0
    
    def parent(self,idx):
        return math.floor((idx-1)/2)
    
    def leftChild(self,idx):
        return idx*2+1
    
    def rightChild(self,idx):
        return idx*2+2
    
    def compare(self,i,j):
        return self.heap[i]>self.heap[j]
        #for min heap change to <
    
    def swap(self,i,j):
        temp=self.heap[i]
        self.heap[i]=self.heap[j]
        self.heap[j]=temp
        return

    def push(self,val):
        self.heap.append(val)
        self.shiftUp()
        return
    
    def shiftUp(self):
        nodeidx=self.size()-1
        while nodeidx>0 and self.compare(nodeidx,self.parent(nodeidx)):
            self.swap(nodeidx,self.parent(nodeidx))
            nodeidx=self.parent(nodeidx)
        return

        
    def pop(self):
        if self.isEmpty():
            return None
        if self.size()==1:
            return self.heap.pop()
        self.swap(0,self.size()-1)
        popped_value=self.heap.pop()
        self.shiftDown()
        return popped_value

    def shiftDown(self):
        nodeidx=0
        while ((self.rightChild(nodeidx)<self.size()) and self.compare(self.rightChild(nodeidx),nodeidx)) or ((self.leftChild(nodeidx)<self.size() and self.compare(self.leftChild(nodeidx),nodeidx))):
            greatestnode= self.rightChild(nodeidx) if self.rightChild(nodeidx)<self.size() and self.compare(self.rightChild(nodeidx),self.leftChild(nodeidx)) else self.leftChild(nodeidx)
            self.swap(nodeidx,greatestnode)
            nodeidx=greatestnode

pq = PriorityQueue()
pq.push(15)
pq.push(12)
pq.push(50)
pq.push(7)
pq.push(40)
pq.push(22)

while not pq.isEmpty() :
    print(pq.pop())