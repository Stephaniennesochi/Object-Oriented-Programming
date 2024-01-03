class animal:
    
    def __init__(self, name, color):
        self.name = name
        self.color = color
        
    def bark(self):
        print(f"My name: %s" % self.name)
        print(f"Color: %s" % self.color)
        
class dog(animal):
    pass

object = dog("Jimmy","Dark")
object.bark()
        