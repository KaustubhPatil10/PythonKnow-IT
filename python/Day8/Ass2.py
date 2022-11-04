class Shape:
    def CalculateArea():
        pass
        
        
class circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    
    def CalculateArea(self):
        return 3.14*self.radius*self.radius
class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def CalculateArea(self):
        return self.length*self.breadth
class Square(Shape):
    def __init__(self,side):
        self.side=side
    def CalculateArea(self):
        return self.side*self.side

c1=circle(5)
print(c1.CalculateArea())
r1=Rectangle(3, 6)
print(r1.CalculateArea())
s1=Square(5)
print(s1.CalculateArea())
    
     
        
        