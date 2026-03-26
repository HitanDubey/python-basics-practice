from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod

    def area(self):
        pass

    def perimeter(self):
        pass

class rectange(Shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    

    def perimeter(self):
        return 2 *(self.width + self.height)
    

react = rectange(5,7)
print(f"Area of rectange : {react.area()}")
print(f"Perimeter of rectanxge : {react.perimeter()}")