"""
Variable Scope
"""
"""
b=10

def test_method(b):
    print('Value of local "b" is : '+ str(b))
    b=2
    print('New value of local "b" is : '+ str(b))

print('Value of global "b" is : '+ str(b))
test_method(b)
print('Did the value of global "b" change ?' + str(b))
"""

b=10

def test_method():
    global b
    print('Value of "b" inside the method is : '+ str(b))
    b=2
    print('New value of "b" inside the method is changed to : '+ str(b))

print('Value of global b is : '+ str(b))
test_method()
print('Did the value of global b change ?' + str(b))