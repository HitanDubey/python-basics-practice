class Dog:
    def __init__(self,name,bread,age):
        self.name = name 
        self.bread = bread
        self.age = age
    def  bark(self):
        print("Woff!")
my_dog = Dog("buddy","golden",5)
print(my_dog.name) 
print(my_dog.bread)
print(my_dog.age)
my_dog.bark()   