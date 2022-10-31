a=input("Enter the String: ")
print("String: ",a)
n1=int(input("Enter the IndexNo to be removed: "))
s1=""                                #additional string

s1= a[ :n1] + a[n1+1: ]             #concatination
print(s1)

