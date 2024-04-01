class Stack:
    def __init__(self):
        self.array=[]
        self.length=0
    
    def peek(self):
        print(self.array[-1])

    def push(self,data):
        self.array.append(data)
        self.length+=1
    
    def pop(self):
        if self.length==0:
            return("The array is empty")
        else:
            del self.array[self.length-1]
            self.length-=1

myStack= Stack()
myStack.push(1)
myStack.push(2)
myStack.push(3)
myStack.peek()
myStack.pop()
myStack.peek()



        