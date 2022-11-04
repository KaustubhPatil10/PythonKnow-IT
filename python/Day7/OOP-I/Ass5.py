class Temperature:
    def __init__(self,t):
        self.t=t
        
    def convert_tofaren(self):
        return self.t*(9/5)+32
    
    def convert_tocelcius(self):
        return ((self.t - 32)*5)/9
   
temp=Temperature(25)
print(temp.convert_tocelcius())
print(temp.convert_tofaren())    