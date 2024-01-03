print(f"This program calculates the amount of petrol remaining and the odometer reading.")


class Car:                                # creating a class name
    
    def __init__(self):                  # Defining the methods of the class
        self.__amount = 0
        self.__odometer = 0
        
    def fill_up(self):                                  
        self.__amount = min(60, self.__amount + (60-self.__amount))     # fill up maximum tank capacity
        
    def drive(self,km:int):
        distance_driven = min(km, self.__amount)
        self.__odometer += distance_driven             # Formular to calculate the odometer reading
        self.__amount -= distance_driven                 # Formular to calculate the amount of petrol remaining
        
    def __str__(self):
        
      return f"Car: odometer reading: {self.__odometer} km, amount of petrol remaining: {self.__amount} litres"  # Calling the function
      
car = Car()

print (car)  

car.__amount= 20
car.fill_up() 
car.drive(20)
print(car)

car.drive(50)
print(car)

car.fill_up()
car.drive(10)
print(car)
