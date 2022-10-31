a= input("Enter the String: ")
print("String is : ",a)
s1='aeiouAEIOU'
count =0
for i in a:
    if i in s1:
        count=count + 1
print("count is : ",count)    
