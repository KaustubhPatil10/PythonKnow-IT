m1,m2,m3,m4,m5=input("Enter the marks of 5 Subjects").split()
print(m1,m2,m3,m4,m5)
m1=int(m1)
m2=int(m2)
m3=int(m3)
m4=int(m4)
m5=int(m5)

avg=(m1+m2+m3+m4+m5)/500
print("Average is :",avg)

per=avg*100

print(" Percentage is ",per)

if per>75:
    print("Distinction")
elif per>60:
    print("First Class")
else:
    print("Second Class")
   
