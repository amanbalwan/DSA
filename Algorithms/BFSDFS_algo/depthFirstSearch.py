class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data

class BinarySearchTree:
    def __init__(self):
        self.root=None
    
    def insert(self,data):
        newNode=Node(data)
        if not self.root:
            self.root=newNode
        else:
            current=self.root
            while current is not None:
                if data>current.data:
                    if current.right:
                        current=current.right
                    else:
                        current.right=newNode
                        break

                else:
                    if current.left:
                        current=current.left
                    else:
                        current.left=newNode
                        break
        return
    
    def lookup(self,data):
        current=self.root
        while current:
            if current.data==data:
                print("True")
                return True
            elif data>current.data:
                current=current.right      
            else:
                current=current.left        
        print("False")
        return False

    def remove(self,data):
        if not self.root:
            return False
        current=self.root
        parent=None
        while current:
            if data>current.data:
                parent=current
                current=current.right      
            elif  data<current.data:
                parent=current
                current=current.left      
            elif data==current.data:
                # Option 1: No right child:
                if current.right==None:
                    if parent is None:
                        self.root=current.left
                    elif current.data>parent.data:
                        parent.right=current.left
                    else:
                        parent.left=current.left

                # Option 2: Right child without left child
                elif current.right.left==None:
                    current.right.left=current.left
                    if parent is None:
                        self.root=current.right
                    else:
                        if current.data>parent.data:
                            parent.right=current.right
                        else:
                            parent.left=current.right

                # Option 3: Right child with left child
                else:
                    leftmost=current.right.left
                    leftmostparent=current.right
                    while leftmost.left:
                        leftmostparent=leftmost
                        leftmost=leftmost.left
                    
                    if leftmost.right:
                        leftmostparent.left=leftmost.right
                    
                    leftmost.right=current.right
                    leftmost.left=current.left

                    if parent is None:
                        self.root=leftmost
                        
                    elif current.data>parent.data:
                        parent.right=leftmost
                        
                    else:
                        parent.left=leftmost
                return
               
        return ("Not Found")

    # def dfsInorder(self,queue,list):
    #     if len(queue)==0:
    #         return list
    #     else:
    #         current=queue.pop(0)
    #         if current.left:
    #             queue.append(current.left)
    #             self.dfsInorder(queue,list)
    #         list.append(current.data)
    #         if current.right:
    #             queue.append(current.right)
    #             self.dfsInorder(queue,list)
        
    #     return list

    def dfsInorder(self,node,list):
        if node.left:
            self.dfsInorder(node.left,list)
        list.append(node.data)
        if node.right:
            self.dfsInorder(node.right,list)
        return list
        
    def dfsPostOrder(self,node,list):
        if node.left:
            self.dfsPostOrder(node.left,list)
        if node.right:
            self.dfsPostOrder(node.right,list)
        list.append(node.data)
        return list
    
    def dfsPreOrder(self,node,list):
        list.append(node.data)
        if node.left:
            self.dfsPreOrder(node.left,list)
        if node.right:
            self.dfsPreOrder(node.right,list)
        return list





    def traverse(self,temp):
        a=[]
        if temp:
            a+=self.traverse(temp.left)  
            a.append(temp.data)
            a+=self.traverse(temp.right)
                   
        return a

            


tree=BinarySearchTree()
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)
#tree.lookup(15)
#tree.remove(15)
#tree.lookup(15)
#print(tree.traverse(tree.root))
print(tree.dfsInorder(tree.root,[]))
print(tree.dfsPostOrder(tree.root,[]))
print(tree.dfsPreOrder(tree.root,[]))