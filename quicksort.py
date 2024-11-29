def quicksort(l, low, high):
    # Base case: if the subarray has more than one element
    if low < high:
        # Partition the subarray and get the pivot index
        pi = partition(l, low, high)
        # Recursively sort the elements before the pivot
        quicksort(l, low, pi - 1)
        # Recursively sort the elements after the pivot
        quicksort(l, pi + 1, high)

def partition(l, low, high):
    # Choose the rightmost element as pivot
    pivot = l[high]
    # Initialize the index of smaller element
    i = low - 1
    # Traverse through all elements
    # Compare each element with pivot
    for j in range(low, high):
        if l[j] <= pivot:
            # Swap elements at i and j
            i += 1
            l[i], l[j] = l[j], l[i]
    # Swap the pivot element with the element at i+1
    l[i + 1], l[high] = l[high], l[i + 1]
    # Return the pivot index
    return i + 1

l = [5, 21, 548, 654, 58, 2, 65, 4, 8]
print("Unsorted array:")
for i in range(len(l)):
    print("%d" % l[i], end=" ")
quicksort(l, 0, len(l) - 1)
print("\nSorted array:")
for i in range(len(l)):
    print("%d" % l[i], end=" ")