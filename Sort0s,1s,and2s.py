"""Given an array arr[] containing only 0s, 1s, and 2s. Sort the array in ascending order."""

def sort_array(arr):
    # Initialize pointers
    low = 0
    mid = 0
    high = len(arr) - 1
    
    # Traverse through the array    
    while mid <= high:
        # If the current element is 0, swap it with the element at low pointer
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        # If the current element is 1, move it to the middle pointer
        elif arr[mid] == 1:
            mid += 1
        # If the current element is 2, swap it with the element at high pointer
        elif arr[mid] == 2:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    
    return arr

# Test the function 
                   
arr = [0, 1, 2, 0, 1, 2, 0, 1, 2]
sorted_arr = sort_array(arr)
print(sorted_arr)  # Output: [0, 0, 0, 1, 1, 1, 2, 2, 2]

# Test the function with an empty array  
arr = []
sorted_arr = sort_array(arr)
print(sorted_arr)  # Output: []
