class temp:
    def __init__(self,cel):
        self.cel = cel


    def f_fern(cls,faharan):
        cels = (faharan-32)*5/9
        return cls(cels)

te = temp.f_fern(98.6)
print(te)    
     