class engine:
    def engine_type(self):
        return "vb"

class body:
    def vip(self):
        return "bbg"

class car(engine,body):
    def car_type(self):
        return "sports car" 

obj = car()
print(obj.car_type())
print(obj.vip()) 
print(obj.engine_type())          