"""
Iterating multiple lists at the same time
"""

l1 = [1,2,15,4]
l2 = [5,6,7,8, 11]
"""
for  a,b in zip(l1,l2):
    print(a)
    print(b)
"""
for  a,b in zip(l1,l2):
    if a > b:
        print(a)
    else:
        print(b)