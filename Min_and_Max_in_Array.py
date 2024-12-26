"""Given an array arr. Your task is to find the minimum and maximum elements in the array.

Note: Return an array that contains two elements the first one will be a minimum element and the second will be a maximum of an array."""
def get_min_max(arr):
        
        a=min(arr)
        b=max(arr)
        return a, b
    
# Test the function

arr = [1, 2, 3, 4, 5]

print(get_min_max(arr)) # Output: (1, 5)

arr = [-10, -20, -30, -40, -50]