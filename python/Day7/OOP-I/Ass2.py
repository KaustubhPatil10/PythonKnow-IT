class reverse:                  #constructor
    def __init__(self,s):
        """ this is the information of """
        self.s=s
        
    def rev(self):             #function
        
        d=self.s.split()
        d=d[::-1]
        self.d=(''.join(d))
        return self.d
    
s1=reverse("i love my india")
print(s1.rev())    