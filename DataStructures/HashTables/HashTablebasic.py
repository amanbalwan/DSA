class hashTable:
    def __init__(self,size):
        self.data = [None]*size
    
    def __str__(self):
        return str(self.__dict__)    
    
    def _hash(self,key):
        hash = 0
        for i in range(0,len(key)):
            hash=(hash+ord(key[i])*i)%len(self.data)
        return hash
        

    def set(self,key,value):
        address=self._hash(key)
        if not self.data[address]:
            self.data[address]=[]
        self.data[address].append([key,value])
    
    def get(self,key):
        address=self._hash(key)
        if not self.data[address]:
            return "not found"
        else:
            bucket=self.data[address]
            for i in range(0,len(bucket)):
                if key==bucket[i][0]:
                    return bucket[i][1]
                return "not found"
    
    def key(self):
        keyarr=[]
        for i in range(0,len(self.data)):
            if self.data[i]:
                for j in range(0,len(self.data[i])):
                    keyarr.append(self.data[i][j][0])
        return keyarr

        

    

myHashTable = hashTable(50)
myHashTable.set('grapes',10000)
myHashTable.set('oranges',40)
myHashTable.set('apples',12)
myHashTable.set('mango',100)
print(myHashTable.get('grapes'))
print(myHashTable.get('mango'))
print(myHashTable.key())