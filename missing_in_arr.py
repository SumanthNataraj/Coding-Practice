"""
Missing in Array

You are given an array arr of size n - 1 that contains distinct integers in the range from 1 to n (inclusive). This array represents a permutation of the integers from 1 to n with one element missing. Your task is to identify and return the missing element.
"""
# Note that the size of the array is n-1
def missingNumber( n, arr):
        
        # Calculate the sum of all numbers from 1 to n
    e = n * (n + 1) // 2
    a=0
        # Calculate the sum of the given array
    for i in range(len(arr)):
        a+=arr[i]
            
        
    b=e-a
        
    return b

# Test the function with an example

arr = [1, 2, 4, 5, 6]
res=missingNumber(6, arr)
print(res) # Output: 3
 # The missing element in the array is 3
    # The array represents a permutation of numbers from 1 to 6 with element 3 missing.
    # The sum of all numbers from 1 to 6 is 21, and the sum of the given array is 15.
    # The missing element is 21 - 15 = 6.
    # The array [1, 2, 4, 5, 6] does not represent a permutation of numbers from 1 to 6.
    # The function correctly identifies the missing element.
    # The time complexity of the function is O(n), where n is the size of the array.
    # The space complexity of the function is O(1).
