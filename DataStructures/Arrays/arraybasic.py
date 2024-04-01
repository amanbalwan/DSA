class MyArray:
    def __init__(self):
        self.length = 0
        self.data = {}
    
    def __str__(self):
        #return str(self.__dict__)
        return str([self.data[i] for i in range(self.length)])


    def get(self,index):
        print(self.data[index])

    def push(self,item):
        self.data[self.length]=item
        self.length+=1
    
    def pop(self):
        lastItem = self.data[self.length-1]
        del self.data[self.length-1]
        self.length-=1
        return lastItem
        
    def delete(self,index):
        deletedItem = self.data[index]
        for i in range(index,self.length-1):
            self.data[i]= self.data[i+1]

        del self.data[self.length-1]
        self.length-=1
        return deletedItem
    

arr = MyArray()
arr.push("hello")
arr.push("like")
arr.push("rio")
arr.push("why")
arr.push("wow")
arr.push("yes")
arr.get(1)
arr.pop()
arr.delete(1)
print(arr)