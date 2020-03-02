"""
1. not
2. and
3. or
"""

bool_output1 = True or not False and False
print(bool_output1)

bool_output2 = 10 == 10 or not 10 > 10 and 10 > 10
print(bool_output2)

bool_output3 = (10 == 10 or not 10 > 10) and 10 > 10
print(bool_output3)
