class student:
    
    def __init__(self,name,regno,dept):
        self.name = name
        self.regno = regno
        self.dept = dept
        
    def show(self):
        print(f"name:{self.name}, regno:{self.regno}")
        
std = student ("Joe","CSC 331","computer science")
print(f'my name is :{std.name}')
print(f'my department is :{std.dept}')
std.show()


class employee:
    
    def __init__(self, name, Id, salary):
        self.name = name
        self.__Id = Id
        self.__salary = salary
        
emp = employee("Steph","0001",1000)
emp1 = employee("Chika","0002",2000)

print(f"my name is %s:" % emp.name)
print(f"my staff Id is %s:" % emp._employee__Id)
print(f"my salary is %s :" % emp._employee__salary)

print(f"my name is %s:" % emp1. name)
print(f"my staff Id is %s:" % emp1._employee__Id)
print(f"my salary is %s :" % emp1._employee__salary)