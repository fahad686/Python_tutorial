def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        current = arr[i]
        j = i - 1
        while j >= 0 and current < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current

# Example usage:
arr = [9, -111, 1, 70, 6]
print("Original array:", arr)
insertion_sort(arr)
print("Sorted array:", arr)
