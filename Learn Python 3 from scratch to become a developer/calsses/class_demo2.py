"""
Object Oriented Programming
"""

class Car(object):
    def __init__(self, make, model):
        self.make = make
        self.model = model

c1 = Car('BMW','550i')
print(c1.make)
print(c1.model)
c2 = Car('Benz' , 'E350')
print(c2.make)
print(c2.model)