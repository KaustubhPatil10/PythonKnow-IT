class Rec:
    def __init__(self,l,b):
        self.l=l
        self.b=b
     
    def area(self):
        return  self.l*self.b
    
a=Rec(5, 6)
print(a.area())
    