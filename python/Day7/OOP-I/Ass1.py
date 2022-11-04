class python:
    def __init__(self,x,n):
        print("Constructor")
        self.x=x
        self.n=n
    
    def pow(self):
        return self.x**self.n
    
     
p=python(5,3)
print(p.pow())