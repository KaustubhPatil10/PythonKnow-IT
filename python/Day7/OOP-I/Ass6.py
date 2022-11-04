class Student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        
    def display(self):
        return self.name,self.rollno
    
    def setAge(self,age):
        self.age=age
        
    def setMarks(self,marks):
        self.marks=marks
        
    def getAge(self):
        return self.age
       
    def getMarks(self):
        return self.marks
    

s=Student("vaibhav",52)
print(s.display())
s.setAge(25)
print(s.getAge())
s.setMarks(85)
print(s.getMarks())

       
        
       