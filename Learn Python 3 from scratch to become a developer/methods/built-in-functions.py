"""
Some Built in functions
max() : It takes any number of arguments and returns the largest one.

min() : It takes any number of arguments and returns the smallest one.

abs() : It returns the absolute value of the number, that number's distance from 0.
It always return a positive value and it only takes a single number.

type() : It returns the type of the data it receives as an argument.
"""

def largest_num(*args):
    #print(max(args))
    return max(args)

# largest_num(-20,-2,0,99)
x = largest_num(-20,-11,0,3,2)
print(str(x))

print('*'*100)

def smallest_num(*args):
    #print(min(args))
    return min(args)

#largest_num(-20,-2,0,99)
x = smallest_num(-20,-11,0,3,2)
print(str(x))

def abs_function (n):
    print(abs(n))

abs_function(-20)
abs_function(20)

print('*'*100)

print(type(99))
print(type(99.9))
print(type('99.9'))

l =  [1,2,3]
print(type(l))
