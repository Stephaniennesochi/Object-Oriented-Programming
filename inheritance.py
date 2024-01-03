class animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        
    def bark(self):
        print(f"My name is {self.name}")
        print(f"My color is {self.color}")
              
class dog(animal):
     def dogbark(self):
        print("Whop! Whop!")
    
object = dog("Jimmy", "Dark")
object.bark()
object.dogbark()