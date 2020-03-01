"""
Dictionary Methods
"""

car = { 'make':'bmw' , 'model':'550i' , 'year':2016 }
cars = { 'bmw' : { 'model': '550i' , 'year' : 2016 } , 'benz' : { 'model': 'E350' , 'year' : 2017 } }

print(car.keys())
print(cars.keys())

print(car.values())
print(cars.values())

print(car.items())
print(cars.items())

copie =  car.copy()
print(copie)

#car.clear()
#print(car)

print(car.pop('model'))
print(car)