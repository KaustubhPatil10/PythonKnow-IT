a=int(input("Enter the number: "))
print(a)
rev=0
while a!=0:
    mod=a%10
    rev=(rev*10)+mod
    a=a//10
else:
    print("Reverse no is : ",rev)
