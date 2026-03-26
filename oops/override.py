class animal:
    def sound(self):
        return f"some generic sound"
class dog(animal):
    def sound(self):
        return f"bark"
class cat(animal):
        def sound(self):
            return f"meow"   

animals = [animal(),dog(),cat()]
for i in animals:
     print(i.sound())         
        
obj = animal()
print(obj.sound())
obj1 = dog()
print(obj1.sound())
obj2 = cat()
print(obj2.sound()  )      