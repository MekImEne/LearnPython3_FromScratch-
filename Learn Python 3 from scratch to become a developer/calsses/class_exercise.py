"""
Exercise
--------
Create a class Fruit
********************
Define 3 methods in this class :
    1. __init__()
    2. nutrition ()
    3. fruit_shape()
Print anything you like in these methods

Create one more class (any fruit name)
This class should inherit from the Fruit class created above, this will become the  child class and 'Fruit' will be
referred as parent class to this class
Define 3 methods in this class
    1. __init__()
    2. nutrition ()
    3. color()
Print anything you like in these methods

Created instances of these classes and call methods from them
Call methods from the base class also using the instance of the child class
"""

class Fruit(object):
    print('I am a fruit !')

    def nutrition(self):
        print('I am full of vitamins')

    def fruit_shape(self):
        print('Every fruit can have a different shape')


class Orange(Fruit):

    def __init__(self):
        Fruit.__init__(self)
        print('I am Orange')

    def nutrition(self):
        print('I am full of vitamin C')

    def color(self):
        print('I keep it simple, the color is also orange !')


f = Fruit()
f.nutrition()
f.fruit_shape()

o = Orange()
o.nutrition()
o.fruit_shape()
o.color()
