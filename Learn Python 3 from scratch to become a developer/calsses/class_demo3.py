"""
Object Oriented Programming
"""

class Car(object):

    Wheels = 4

    def __init__(self, make, model):
        self.make = make
        self.model = model

    def info(self):
        print('Make of the car : ' + self.make)
        print('Model of the car : ' + self.model)

c1 = Car('BMW','550i')
c1.info()
print(c1.Wheels)

c2 = Car('Benz' , 'E350')
c2.info()
c2.Wheels = 22
print(c2.Wheels)

print(Car.Wheels)
