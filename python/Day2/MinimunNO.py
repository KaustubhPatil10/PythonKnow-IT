n1,n2,n3=input("Enter 3No's: ").split()
print(n1,n2,n3)
n1=int(n1)
n2=int(n2)
n3=int(n3)

if n1<n2 and n1<n3:
        print(n1,"is smaller")
elif   n2<n3 and n2<n1:
        print(n2,"is smaller")
else:
        print(n3,"is smaller")
