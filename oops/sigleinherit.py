class vehicle:
    def __init__(self,brand , model):
        self.brand = brand
        self.model = model
    
    def desc(self):
        return f"{self.brand}  {self.model}"

class car(vehicle):
    def wheels(self):
        return 4
my_car = car("toyta","corolla")  
print(my_car.desc())
print(my_car.wheels())      



