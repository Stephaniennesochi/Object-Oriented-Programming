class employee:
    def __init__(self,Id, name):
        self.__Id = Id
        self.name = name
        
    def getId(self):
        return self.__Id
    
    def setId(self,Id):
        self.__Id = Id
        
emp = employee ("0001","Uju")
print(f"name:{emp.name}")
print(f"Id:{emp.getId()}")

emp.setId("0002")
print(f"name:{emp.name}")
print (f"Id: {emp.getId()}")
