class animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        
    def bark(self):
        print(f"My name is {self.name}")
        print(f"My color is {self.color}")
              
class dog(animal):
     def bark(self):
        print("Whop! Whop!")
        super().bark()    
        
object = dog("Jimmy", "Dark")
object.bark()
object.bark()