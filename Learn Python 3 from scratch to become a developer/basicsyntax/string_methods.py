"""
Examples to show available string methods in Python
"""

# Accessing characters in a string
first = "imene"[0]
#index starts from zero in python
print(first)

second = "abdou"
s=second[0]
print(s)
print("*****************************************************************************************************")
"""
Functions with strings  :
len()
lower()
upper()
str()
"""

s= 'ThiS Is a MiXed CaSE'
print(s.lower())
print(s.upper())
print(len(s))
print(s + str(2))


"""
Concatenation
"""
print("Hello " + " " + " World !")
print(first + " l " + second)


print("***************************************************************************************************************")

# Replace Method
a= "1abc2abc3abc4abc5abc"
print(a.replace('abc', 'IMENE'))
print(a.replace('abc', 'IMENE', 1))
print("***************************************************************************************************************")
# Sub-Strings Method
# Starting index is inclusive
# Ending index is exclusive
sub = a[1:7]
step1 = a[1:7:1]
step2 = a[1:7:2]
print(sub)
print(step1)
print(step2)
print("***************************************************************************************************************")
"""
More String Slicing And Indexing
"""
St = "This is a string"
print(St[:])
print(St[1:])
print(St[:6])
print(St[-1])
print(St[:-2])
print(St[:len(St)])
print(St[:len(St)-3])
print(St[::])
print(St[::1])
print(St[::2])
print(St[::-1])   # MIROIR
print(St[0])


