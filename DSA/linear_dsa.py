# #1. Arrays (Lists in Python)
# #An array is a collection of elements stored contiguously in memory. In Python, lists behave like dynamic arrays.List can store multitype of data
#
list=[7,0,3,'Fahad',1,5]
#
arr=[1,9,3.0,7]
# print(arr)
#
# print(list)
#
# #Accessing element by index
# print(arr[2])
#
# #Accessing element by negative index
# print('Accessing element by using negative index \n',arr[-2])
#
# #Modifying element
# arr[2]=10
# print(arr)
#
# #adding or appending a new element in list
# arr.append(900)
# print(arr)

#Tuple
#Python tuples are similar to lists but Tuples are immutable in nature i.e. once created it cannot be modified. Just like a List, a
# Tuple can also contain elements of various types.
#In Python, tuples are created by placing a sequence of values separated by ‘comma’ with or without the use of parentheses for grouping
# of the data sequence.

# Creating a Tuple with
# the use of Strings
# Tuple = ('Geeks', 'For')
# print("\nTuple with the use of String: ")
# print(Tuple)
#
# # Creating a Tuple with
# # the use of list
# list1 = [1, 2, 4, 5, 6]
# print("\nTuple using List: ")
# Tuple = tuple(list1)
#
# # Accessing element using indexing
# print("First element of tuple")
# print(Tuple[0])
#
# # Accessing element from last
# # negative indexing
# print("\nLast element of tuple")
# print(Tuple[-1])
#
# print("\nThird last element of tuple")
# print(Tuple[-3])

#
# Set
# Python set is a mutable collection of data that does not allow any duplication. Sets are basically used to include membership
# testing and eliminating duplicate entries. The data structure used in this is Hashing, a popular technique to perform insertion,
# deletion, and traversal in O(1) on average.

# Creating a Set with
# a mixed type of values
# (Having numbers and strings)
aa = set([1, 2, 'fahad', 4, 'ali', 6, 'ali'])
print("\nSet with the use of Mixed Values")
print(aa)


# Accessing element using
# for loop
print("\nElements of set: ")
for i in aa:
    print(i, end =" ")
print()

# Checking the element
# using in keyword
print("hassan" in aa)









#--------------------------------------------------Sorting technique-------------------------------------------------------------#
#
# #sorting list in ascending order
# arr.sort()
# print("         Sorting    \n\nAscending order\n",arr)
#
# #sort list in descending order
# arr.reverse()
# print("Descending order\n",arr)
#
# sorted_arr=sorted(arr)
# print("Return a new sorted list \n",sorted_arr)
#
# sorted_desc_arr=sorted(arr,reverse=True)
# print("Return a new Descending  sorted list \n",sorted_desc_arr)


