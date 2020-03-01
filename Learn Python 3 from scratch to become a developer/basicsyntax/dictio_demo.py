"""
Data type to store more than one value in one variable name
Dictionary items are in brackets {} in key:value pairs, separated with " , " { 'k1' : 'v1' , 'k2' : 'v2' }
Not sequenced, no indexing -> Mapping
"""
car = {'make':'bmw' , 'model':'550i' , 'year':2016}
print(car)
print(car['make'])
model = car['model']
print(model)

d = {} # dictionnaire vide
print(d)
d['one']=1
d['two']=2
print(d)

somme = d['two'] + 8
print(somme)
print(d)

d['two'] = d['two']+8
print(d)