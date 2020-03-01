"""
Built-in methods to help manipulating a list
"""
cars = [ "BMW" , "Honda" , "Audi"]

length = len(cars)
print(length) # la longueur de la liste

cars.append('Benz')
print(cars) # insérer un objet à la fin

cars.insert(1, 'Jeep')
print(cars) # insérer un objet à la position 1

x = cars.index('Honda')
print(x)

y = cars.pop()  # Supprimer le dernier element de la liste
print(y)
print(cars)

cars.remove('Jeep') # Supprimer un element donné de la liste
print(cars)

slicing = cars[0:2]
a = cars[1:]
print(slicing)
print(a)

print('*'*150)
print(cars)
cars.sort() # Ordonner la liste un ordre alphabétique
print(cars)