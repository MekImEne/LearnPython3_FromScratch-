"""
https://docs.python.org/3/library/
"""

import  math
# from math import  sqrt
#import modulesexternal.car as car
from modulesexternal import car

class ModulesDemo ():
    def builtin_modules(self):
        print(math.sqrt(100))
        # print(sqrt(10000))

    def car_description(self):
        make = 'bmw'
        model = '550i'
        car.info(make, model)


m = ModulesDemo()
m.builtin_modules()
m.car_description()

