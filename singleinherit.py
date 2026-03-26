class animal:
    def __init__(self,name):
        self.name = name 
    def speak(self):
        print("Generic sound")

class dog(animal):
    def speak(self):
        print("woff!")
my_dog = dog("buddy")
my_dog.speak()
print(my_dog.name)        