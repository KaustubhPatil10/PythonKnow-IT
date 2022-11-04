class time:
    def __init__(self,hh,mm):
        self.hh=hh
        self.mm=mm
        
    def addTime(self,t1,t2):
        t3=time(0,0)
        t3.hh=t1.hh+t2.hh
        t3.mm=t1.mm+t2.mm
        return t3
    
    def __str__(self):
     return f'{self.hh} ,{self.mm}'
 
    def displayminute(self,t3):
        for i in range(t3.hh):
           t3.mm=t3.mm+60
        return f'{t3.mm}minutes'
    def displaytime(self,t3):
        if t3.mm>60:
            t3.hh=t3.hh+1
            t3.mm=t3.mm-60
            return f'{t3.hh},{t3.mm}'
        
        
        
t1=time(2,2)
print(t1)
t2=time(3,3)
print(t2)
t3=t1.addTime(t1,t2)
print(t3)  
t4=t1.displayminute(t3)
print(t4)
t5=t1.displaytime(t3)
print(t5)
    
    
        