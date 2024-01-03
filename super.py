class  animal:
    def __init__(self, name,color):
        self.name = name
        self.color = color
        
    def bark(self):
        print (f"My name is {self.name}")
        print (f"My color is {self.color}")
        
class dog(animal):
    def __init__(self,name,color,breed):
        
        super().__init__(name,color)
        self.breed = breed
        
    def dogbark(self):
        print (f"My breed is {self.breed}")
        
object = dog("Jimmy", "Dark","German Sherpherd")
object.bark()
object.dogbark()
        