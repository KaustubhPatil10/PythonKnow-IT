a=input("Enter the String: ")
print("String is: ",a)
countU=0
countL=0
for i in a:
    if i.isupper():
        countU=countU+1
    elif i.islower():
        countL=countL+1
print("Upper case count: ",countU)
print("Lower case count: ",countL)
        
        
