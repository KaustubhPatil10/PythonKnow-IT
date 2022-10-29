a=int(input("Enter the number: "))
print(a)
rev=0
temp=0
while a!=0:
    mod=a%10
    rev=(rev*10)+mod
    a=a//10
    temp=rev
if rev==temp:
     print("Entered no is palindrome")
else:
     print("Entered  is not a palindrome")
        
