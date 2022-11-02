def overlapping(l1,l2):
    for i in l1:
        if i in l2:
            return True
        else:
            return False
        
l1=[1,2,3,4,5,6,7,8]
l2=[9,2,3,11,12,13,14,8]
l3=[1,2,3,4]
print(overlapping(l1, l3))    
    