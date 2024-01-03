class course:
    def __init__(self,code,title,lecturer):
        self.code = code
        self.title = title
        self.lecturer =lecturer
    def displaycourse(self):
        print(f"The title of the course is: %s" % self.title)
        print(f"The course code is: %s" % self.code)
        print(f"The lecturer is: %s" % self.lecturer)
course1 = course('CSC 331','Object-oriented Programming','Mr Benjamin')
course1.displaycourse()


class employee:
    
    def __init__(self,Id,name,salary):
        self.name = name
        self.Id = Id
        self.salary = salary
        
    def show(self):
        print(f"my name is %s:" % self.name)
        print(f"my id is %s:" % self.Id)
        print(f"salary paid is %s:" %self.salary)
emp = employee("0001","Steph",1000)
emp.show()