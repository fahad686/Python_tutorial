# _________________________________________________________________ Linear dsa ____________________________________________________________________________________#

# Sorting and searching can be achieved in Python through the use of simple statements and algorithms. A sorting
# algorithm is used to rearrange a given list or an array of elements in a defined order, either increasing or  decreasing.
# A searching algorithm is used to check the presence of a component in a list or array and displays the
# position of the element in the list or array or will return a False if it is non-existent in the list. In this
# article, we are discussing the basic Sorting Algorithms and Searching Algorithms in Python.

# Part 1 is Sorting Algorithms and Part 2 is Searching algorithms

# Sorting Algorithms Let us begin with a sorting algorithm. We all know that python comes with an inbuilt function to
# sort an array of numbers.

array = [64, 34, 25, 12, 22, 11, 90]

print("Array before sorting:", array)

# Dictionary


meta = {'wa': 'WhatsApp', 'fb': 'Facebook', 'ig': 'Instagram'}
print(meta)

print(meta['fb'],meta['ig'])




# -------------------------------------------------------Bubble sorting -------------------------------------------------------------------- #
class SortingAlgorithms:
    @staticmethod
    def bubbleSort(array):

        # loop to access each array element
        for i in range(len(array)):

            # loop to compare array elements
            for j in range(0, len(array) - i - 1):

                # compare two adjacent elements
                # change > to < to sort in descending order
                if array[j] > array[j + 1]:
                    # swapping elements if elements
                    # are not in the intended order
                    array[j] , array[j+1] = array[j+1], array[j]
                    # temp = array[j]
                    # array[j] = array[j + 1]
                    # array[j + 1] = temp

    @staticmethod
    def selection_sort(arr):
        n = len(arr)
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_index]:
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]

    @staticmethod
    def insertion_sort(arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

    @staticmethod
    def merge_sort(arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            left_half = arr[:mid]
            right_half = arr[mid:]

            SortingAlgorithms.merge_sort(left_half)
            SortingAlgorithms.merge_sort(right_half)

            i = j = k = 0
            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    arr[k] = left_half[i]
                    i += 1
                else:
                    arr[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                arr[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                arr[k] = right_half[j]
                j += 1
                k += 1

    @staticmethod
    def quick_sort(arr, low, high):
        if low < high:
            pivot = SortingAlgorithms.partition(arr, low, high)
            SortingAlgorithms.quick_sort(arr, low, pivot - 1)
            SortingAlgorithms.quick_sort(arr, pivot + 1, high)

    @staticmethod
    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1


# Example usage
array = [64, 34, 25, 12, 22, 11, 90]

print("Array before sorting:", array)
SortingAlgorithms.bubbleSort(array)
print("Bubble Sort:", array)

array = [64, 34, 25, 12, 22, 11, 90]

print("Array before sorting:", array)
SortingAlgorithms.selection_sort(array)
print("Selection Sort:", array)

array = [64, 34, 25, 12, 22, 11, 90]

print("Array before sorting:", array)
SortingAlgorithms.insertion_sort(array)
print("Insertion Sort:", array)

array = [64, 34, 25, 12, 22, 11, 90]

print("Array before sorting:", array)
SortingAlgorithms.merge_sort(array)
print("Merge Sort:", array)

array = [64, 34, 25, 12, 22, 11, 90]

print("Array before sorting:", array)
SortingAlgorithms.quick_sort(array, 0, len(array) - 1)
print("Quick Sort:", array)
