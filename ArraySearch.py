"""Given an array, arr of n integers, and an integer element x, find whether element x is present in the array. Return the index of the first occurrence of x in the array, or -1 if it doesn't exist."""
def search(self,arr, x):
        # Iterate through the array and check if each element is equal to x
        for i in range(len(arr)):
            if(arr[i]==x):
                return i
        
        return -1

# Test the function

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = 5

result = search(arr, x)
if result != -1:
    print("Element found at index", str(result))
    