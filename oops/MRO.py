class A:
    def greet(self):
        return f"Hello world"
    

class B(A):
    pass

class C(B):
    pass

obj =  C()
print(obj.greet())
print(C.__mro__)

class X:
    def great(self):
        return f"Hello world from down a"

class Y:
    pass

class Z(X,Y):
    pass

obj1 = Z()
print(obj1.great())
print(Z.__mro__)
    

    