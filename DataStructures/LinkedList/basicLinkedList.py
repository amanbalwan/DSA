class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=self.head
        
        
    def append(self,data):
        if not self.head:
            newNode=Node(data)
            self.head = newNode
            self.tail=self.head
            self.length=1
        else:
            newNode=Node(data)
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
            newNode.next=temp.next
            temp.next=newNode
            self.length+=1
   
    def prepend(self,data):
        newNode = Node(data)
        newNode.next=self.head
        self.head=newNode
        self.length+=1

    def remove(self,index):
        if index>=self.length:
            print("index out of bound")
            return 
        elif index==0:
            self.head=self.head.next
            self.length-=1
        # elif index==self.length-1:
        #     self.tail.next=None
        #     self.length-=1
        else:
            temp=self.head
            for i in range(0,index-1):
                temp=temp.next
            temp.next=temp.next.next
            self.length-=1

    def reverse(self):
        prev=None
        curr=self.head
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        self.head,self.tail=self.tail,self.head
        

            


    def print(self):
        temp=self.head
        arr=[]
        while temp is not None:
            arr.append(temp.data)
            temp=temp.next
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
ll.reverse()
ll.print()
