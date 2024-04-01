class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Stack:
    def __init__(self):
        self.top=None
        self.bottom=None
        self.length=0
    
    def push(self,data):
        newNode=Node(data)
        if self.bottom==None:
            
            self.bottom=newNode
            self.top=newNode
    
        else:
            
            newNode.next=self.top
            self.top=newNode
            
        self.length+=1

    def peek(self):
        if self.top:
            print(self.top.data)
        else:
            print("empty stack")
            
    def pop(self):
        if self.top:
            self.top=self.top.next
            self.length-=1
            if self.length==0:
                self.bottom=None
        else:
            print("stack is empty")
            

            
        
    
myStack = Stack()
myStack.push(1)
myStack.push(2)
myStack.push(3)
myStack.peek()
myStack.pop()
myStack.peek()
myStack.pop()
myStack.peek()
myStack.pop()
myStack.peek()
myStack.push(4)
myStack.push(5)
myStack.peek()

