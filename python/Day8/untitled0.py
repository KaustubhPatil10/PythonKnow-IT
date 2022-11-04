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