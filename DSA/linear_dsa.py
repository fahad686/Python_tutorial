#1. Arrays (Lists in Python)
#An array is a collection of elements stored contiguously in memory. In Python, lists behave like dynamic arrays.List can store multitype of data

list=[7,0,3,'Fahad',1,5]

arr=[1,9,3.0,7]
print(arr)

print(list)

#Accessing element by index
print(arr[2])

#Accessing element by negative index
print('Accessing elemnt by using negative index \n',arr[-2])

#Modifying element
arr[2]=10
print(arr)

#adding or appending a new element in list
arr.append(900)
print(arr)



#--------------------------------------------------Sorting technique-------------------------------------------------------------#

#sorting list in accending order
arr.sort()
print("         Sorting    \n\nAscending order\n",arr)

#sort list in decending order
arr.reverse()
print("Descending order\n",arr)

sorted_arr=sorted(arr)
print("Return a new sorted list \n",sorted_arr)

sorted_desc_arr=sorted(arr,reverse=True)
print("Return a new Descending  sorted list \n",sorted_desc_arr)
