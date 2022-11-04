class person:
    def __init__(self,pid,name,emailid,mobno):
        self.pid=pid
        self.name=name
        self.emailid=emailid
        self.mobno=mobno
        
    def display(self):
        return f'{self.pid},{self.name},{self.emailid},{self.mobno}'

p1=person(101, "Kaustubh", "kp1gmailcom", 8855229301)
print(p1.display())

print('='*35)

class Employee(person):
    def __init__(self,Dept,desig,salary):
        self.Dept=Dept
        self.desig=desig
        self.salary=salary
        
    def setDept(self,Dept):
        self.Dept=Dept
    
    def setdesig(self,desig):
        self.desig=desig    
        
    def setsalary(self,salary):
        self.salary=salary 
        
    def getDept(self):
        return self.Dept
    
    def getdesig(self):
        return self.desig
    
    def getsalary(self):
        return self.salary
    
    def display(self):
        return f'{self.Dept},{self.desig},{self.salary}'
    
    def calculateNetsal(self):
        return f'{self.salary+self.salary*0.20}'

e1=Employee("Mechanical","Assistant Engineer",15000)
print(e1.display())
print(e1.calculateNetsal())
e1.setsalary(20000)
e1.setDept("Electronics")
e1.setdesig("Labour")
e1.getDept()
e1.getdesig()
e1.getsalary()
print(e1.display())
print(e1.calculateNetsal())


print('='*35)


class Member(person):
    def __init__(self,membertype,amtpaid):
        self.membertype=membertype
        self.amtpaid=amtpaid
        
    def setmembertype(self,membertype):
        self.membertype=membertype
        
    def seamtpaid(self,amtpaid):
        self.amtpaid=amtpaid
        
    def getmembertype(self):
        return self.membertype
    
    def getamtpaid(self):
        return self.amtpaid
    
    def display(self):
        return f'{self.membertype},{self.amtpaid}'
    
m1=Member("seniorEmployee","75000")
print(m1.display())   
            
    
        
        