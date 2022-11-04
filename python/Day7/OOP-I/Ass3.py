class String:
    def __init__(self,a):
        self.a=a
        
    def get_String(self):
        return self.a
    
    def print_String(self):
        c=self.a.upper()
        print(c)
        
        
b=String("vaibhav")
b.print_String()
