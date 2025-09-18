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


######### list

x = ["apple", "banana", "cherry"]
print(x)
print(type(x))


#############
x = ("apple", "mango", "cherry")
print(x)
print(type(x))


########## range  its  start from 0 ....

x_range=range(10)
print(x_range)
print(type(x_range))

########### dic its stor value as  map like key value


x = {"name" : "John", "age" : 36}
print(x)
print(type(x))


######## set
x = {"apple", "banana", "cherry"}
print(x)
print(type(x))


######### frozenset
x = frozenset(("apple", "banana", "cherry")) ##	frozenset
print(x)
print(type(x))

##### bytes
x = b"Hello"
v=bytes(5)
print(v)
print(x)

############## bytearray
x = bytearray(5)
print(x)


########### memoryview
x = memoryview(bytes(5))
print(x)


###### None
x = None
print(x)
x=3
print(x)