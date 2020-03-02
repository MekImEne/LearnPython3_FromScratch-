"""
Positional Parameters
They are like optional parameters
and can be assigned a default value , if no value is provided from outside
"""
def sum_nums(n1=2,n2=4):
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
s2 = sum_nums()
print(s2)
s3 = sum_nums(n1=8, n2=3)
print(s3)
s4 = sum_nums(n2=9)
print(s4)
s5 = sum_nums(4, n2=15)
print(s5)
