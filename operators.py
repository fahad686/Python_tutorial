# Arithmatic Operators  (=,-,*,/,**,//,%)
print('"""""""""""""""Arithmatic operators""""""""""""""""""""""')
num1=9
print("num1 is : ",num1)
num2=2
print("num2 is : ",num2)
print(' Multiplication of num1 * num2  = ', num1+num2)
print(' Addition of num1 * num2        = ', num1*num2)
print(' Subtraction of num1 * num2     = ', num1-num2)
print(' Division of num1 * num2        = ', num1/num2)
print(' Moduls of num1 * num2          = ', num1%num2)
print(' Float division num1 * num2     = ', num1//num2)
print(' Square of  num1 * num2         = ', num1**num2)

# Assignment Operators(=,+=,-=,/=)
print('""""""""""""""" Assignment Operators """"""""""""""""""""""')
a=3
print(a)
a+=3
a-=2
a/=2
a%=2
a**=2
a//=2# Float Division its mean that after decimal value will remove
print(a)
#Comparison Operators (==,<,>,!=)
print('""""""""""""""" Comparison Operators """"""""""""""""""""""')
a=7
b=5
print("print True if a is equal to b:             ",a==b)
print("print True if a is not equal to b:         ",a!=b)
print('print True a less form b:                  ',a<b)
print("print True a grater from b:                ",a>b)
print("print True a grater then and equal to b:   ",a>=b)
print("print True a less then and equal to  b:    ",a<=b)

print('""""""""""""""" Logical Operators """"""""""""""""""""""')
a=4
b=7
print(a==b and a<b)
print(a<b and b>a)
print(a==b or a<b)
print(not(a==b))
c=(a==b or a<b)
print("c Value is  ",c)
print('after not c value is: ',not(c))



############ Python Identity Operators   "is"  return true if belong to same object(like x is y) / "is not" return True if both value  are not same belong to same object( x is not y)
#Identity operators are used to compare the objects, not if they are equal, but if
# they are actually the same object, with the same memory location:



x=10
y=10

print(x is y) ## belong to same object
print(x is not y) ### not belong to same object

print(x==y)



'''Python Membership Operators  rcrdsidn
Membership operators are used to test if a sequence is presented in an object:'''
'''in 	Returns True if a sequence with the specified value is present in the object	x in y'''


name=['fahad','ali',9]
print(9 in name)  ## Return True

print('Kiran' in name) ## Return False



'''
not in	Returns True if a sequence with the specified 
value is not present in the object	x not in y'''

print(8 not in name) ## return True