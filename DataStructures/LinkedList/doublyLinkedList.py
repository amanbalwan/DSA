class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=self.head
        self.prev=None
        
    def append(self,data):
        if not self.head:
            newNode=Node(data)
            self.head = newNode
            self.tail=self.head
            self.length=1
        else:
            newNode=Node(data)
            newNode.prev=self.tail
            self.tail.next=newNode
            self.tail=newNode
            self.length+=1
    
    def insert(self,index,data):
        if index>=self.length:
            print("index out of bound")
            return 
        elif index==0:
            self.prepend(data)
        elif index==self.length:
            self.append(data)
        else:
            temp=self.head
            for i in range(0,index-1):
                temp=temp.next
            newNode=Node(data)
            temp.next.prev=newNode
            newNode.prev=temp
            newNode.next=temp.next
            temp.next=newNode
            self.length+=1
   
    def prepend(self,data):
        newNode = Node(data)
        self.head.prev=newNode
        newNode.next=self.head
        self.head=newNode
        self.length+=1

    def remove(self,index):
        if index>=self.length:
            print("index out of bound")
            return 
        elif index==0:
            self.head=self.head.next
            self.head.prev=None
            self.length-=1
        # elif index==self.length-1:
        #     self.tail.next=None
        #     self.length-=1
        else:
            temp=self.head
            for i in range(0,index-1):
                temp=temp.next    
            temp.next=temp.next.next
            temp.next.prev=temp
            self.length-=1

    def print(self):
        temp=self.head
        arr=[]
        while temp is not None:
            arr.append(temp.data)
            temp=temp.next
        print(arr)

    def reverseprint(self):
        temp=self.tail
        arr=[]
        while temp is not None:
            arr.append(temp.data)
            temp=temp.prev
        print(arr)
            

    

            
            

            

ll=LinkedList()
ll.append(2)
ll.append(3)
ll.append(5)
ll.print()
ll.prepend(1)
ll.print()
ll.insert(3,4)
ll.print()
ll.remove(3)
ll.print()
ll.reverseprint()
