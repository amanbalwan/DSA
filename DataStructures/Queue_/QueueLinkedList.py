class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Queue:
    def __init__(self):
        self.first= None
        self.last=None
        self.length=0

    def enqueue(self,data):
        newNode= Node(data)
        if self.length==0:
            self.first=newNode
            self.last=newNode
            self.length+=1
        else:
            self.last.next=newNode
            self.last=newNode
            self.length+=1
        
    def dequeue(self):
        if self.first is None:
            return("Queue is empty")

        else:
            self.first=self.first.next
            self.length-=1

    def peek(self):
        print(self.first.data)

myQueue = Queue()
myQueue.enqueue("Aman")
myQueue.enqueue("Abhishek")
myQueue.enqueue("mouse")
myQueue.enqueue("hippo")
myQueue.peek()
myQueue.dequeue()
myQueue.peek()
myQueue.dequeue()
myQueue.peek()
myQueue.dequeue()