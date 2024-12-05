"""Given an array arr[] and an integer k where k is smaller than the size of the array, the task is to find the kth smallest element in the given array."""

def find_kth_smallest(arr, k):
    # Sort the array in ascending order
    arr.sort()
    
    # Return the kth smallest element
    return arr[k-1]

# Test the function 

arr = [5, 2, 8, 1, 3, 6, 4]
k = 3

result = find_kth_smallest(arr, k)
print(f"The {k}th smallest element is: {result}")