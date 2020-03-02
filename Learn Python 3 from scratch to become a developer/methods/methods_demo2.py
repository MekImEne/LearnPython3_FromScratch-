"""
a group of code statements which can perform some specific task
Methods are reusable and can be called when needed in the code
"""

def sum_nums(n1,n2):
    """
    Get sum of two numbers
    :param n1:
    :param n2:
    :return:
    """
    #print(n1+n2)
    return  n1+n2
s1 = sum_nums(11,4)
print(s1)

s2 = sum_nums(2,8)
print(s2)

string_add = sum_nums('one', 'two')
print(string_add)

print('*'*100)

def isMetro(city):
     l = ['sfo', 'nyc', 'lo']

     if city in l:
         return True
     else:
         return False

x = isMetro('lo')
print(x)