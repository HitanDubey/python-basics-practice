class person:
    count = 0

    def __init__(self,name):
        self.name = name
        person.count +=1

    @classmethod
        
    def get_count(vip):
        return vip.count

p1 = person("hello")
p2 = person("World")
print(person.get_count())    
