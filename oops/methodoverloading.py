class Bird:
    def fly(self):
        return f"Bird is flying"

class sparrow(Bird):
    def fly(self):
        return f"Sparrow is flying"


class Ostrich(Bird):
    def fly(self):
        return f"ostrich is flying"

def make_fly(bird):
    print(bird.fly())

spa = sparrow()
ost = Ostrich()
print(spa.fly())
print(ost.fly())
make_fly(spa)
make_fly(ost)