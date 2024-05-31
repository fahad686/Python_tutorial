


 # -------------------------------------------------------- Bubble Sort ----------------------------------------------------------------------------#

# Working of Bubble Sort
# Suppose we are trying to sort the elements in ascending order.
#
# 1. First Iteration (Compare and Swap)
#
# Starting from the first index, compare the first and the second elements.
# If the first element is greater than the second element, they are swapped.
# Now, compare the second and the third elements. Swap them if they are not in order.
# The above process goes on until the last element.


def bubble_sort(list1):
    for i in range(len(list1)):
        for j in range(0,len(list1)-i-1):
            if list1[j] > list1[j+1]:
                temp=list1[j]
                list1[j] = list1[j+1]
                list1[j+1] = temp


list=[7,3,9,1,-10,0]
bubble_sort(list)
print('Sorted List by Bubble sort:')
print(list)

