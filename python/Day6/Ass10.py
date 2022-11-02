def Square(n):
    return n*n

l1=[1,2,3,4,5,6,7,8,9,10]
for i in l1:
    print(Square(i))

l2=list(map(Square, l1))
print(l2)