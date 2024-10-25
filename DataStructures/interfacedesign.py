class Person:
    def __init__(self,name):
        self.name=name
        self.children=[]
        self.alive=True
    
class Monarchy:
    def __init__(self,king):
        self.king=Person(king)
        self.persons={self.king.name:self.king}

    def birth(self,childname,parentname):
        parent=self.persons[parentname]
        child=Person(childname)
        parent.children.append(child)
        self.persons[childname]=child
        
    
    def death(self,name):
        try:
            if self.persons[name]:
                self.persons[name].alive = False
        except:
            return None
    
    def dfs(self,person,order):
        if person.alive:
            order.append(person.name)
        for i in person.children:
            self.dfs(i,order)
        return order

    def getOrder(self):
        order=[]
        self.dfs(self.king,order)
        return order
   

m=Monarchy("Aman")
m.birth("Aman1","Aman")
m.birth("Aman12","Aman1")
m.birth("Aman2","Aman")
m.birth("Aman21","Aman2")
m.birth("Aman3","Aman")
print(m.getOrder())