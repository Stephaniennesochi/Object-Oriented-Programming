
        # Inheritance
print("This program uses inheritance to print information of a student")

class student:                                  
    
    def __init__(self,name,regno,dept):
        self.name = name
        self.regno = regno
        self.dept = dept
        
    def show(self):
        print(f"My name is:{self.name}")
        print(f"My regno is:{self.regno}")
        print(f"My dept is:{self.dept}")
        
class students(student):
    
    def show(self):
        print("i am a student of the Godfrey Okoye University")
        super().show()
        
student1= students("Stephanie","CSC 331","computer science")
student1.show()
student1.show()