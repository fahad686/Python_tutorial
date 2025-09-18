from operator import truediv

##string
a='Fahad'
print(a)
print(type(a))

####### int
a=23
print(a)
print(type(a))

##float
a=3.3
print(a)
print(type(a))

###### boolean
a=True #False
print(a)
print(type(a))

##### complex number built
a=7-3j
print(a)
print(type(a))

print(a.real)
print(a.imag)

#we can create real imag
print(complex(11-9))

z3 = complex(4, 6)  # Creates 4 + 6j
z4 = complex(-1, 0)  # Creates -1 + 0j (or just -1)

print(z3)
print(z4)

'''Complex Number Operations:
Arithmetic Operations: Standard operations like addition, subtraction, multiplication, and division work as expected.
Python
'''

c1 = 1 + 2j
c2 = 3 - 4j

print(c1 + c2)  # Addition: (4-2j)
print(c1 - c2)  # Subtraction: (-2+6j)
print(c1 * c2)  # Multiplication: (11+2j)
print(c1 / c2)  # Division: (-0.2+0.4j)