"""
Built-in function
Creates a sequence of numbers but doesnt save them in memory
Very useful for generating numbers
"""

print(list(range(0, 10)))

a = range(12,25)
print(a)
print(type(a))
print(list(a))

b = range(11)
print(list(b))

c= range(1,20,2)
print(list(c))

print('*'*50)

# l=[1,2,3]
# for num in l:
#     print(num)
# same as :
for num in range(1,4):
    print(num)