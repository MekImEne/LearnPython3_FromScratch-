"""
Exercise
--------
Create a dictionary 'car'
Create 3 keys
 - make
 - model
 - year

Try to access the color key. Remember, we never created the color key, so it's going to throw an exception
You need to handle the exception using the try, except and finally block
"""


def exceptionHandling():
    try:
        car = { 'make':'bmw' , 'model':'550i' , 'year':'2016' }
        print(car['color'])
    except:
        print('key not found')
    finally:
        print('Please try a different key')

exceptionHandling()

