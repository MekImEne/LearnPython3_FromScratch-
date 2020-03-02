"""
Execute statements repeatedly
Conditions are used to stop the execution of loops
Iterable items are Strings, List, Tuple, Dictionary
"""
# Strings for loop
my_string = 'imeneMEKIDECHE'
for c in my_string:
    #print(c)
    print(c, end=' ')

print('*'*100)

my_string2 = 'bcbcbcbcbc'
for c in my_string2:
    if c == 'b':
        print('B', end=' ')
    else:
        print(c, end=' ')

print('*'*100)

# List for loop
cars = ['bmw', 'benz' , 'honda']
print(cars)

for car in cars:
    print(car)

print('*'*100)

nums = [1,2,3,4]
for n in nums :
    print(n*10)


print('*'*100)
# Dictionary for loop

d = {'one': 1, 'two':2 , 'three':3}
for k in d:
    print(k + ' ' + str(d[k]))
print('*'*50)
for k,v in d.items():
    print(k)
    print(v)


