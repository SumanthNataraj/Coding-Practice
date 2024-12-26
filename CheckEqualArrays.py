"""Given two arrays arr1 and arr2 of equal size, the task is to find whether the given arrays are equal. Two arrays are said to be equal if both contain the same set of elements, arrangements (or permutations) of elements may be different though.
Note: If there are repetitions, then counts of repeated elements must also be the same for two arrays to be equal."""

def check( arr1, arr2) -> bool:
        # Sort both arrays and compare them for equality
        a=sorted(arr1)
        b=sorted(arr2)
        return a==b

# Test the function 
                   
arr1 = [1, 2, 3, 4, 5]
arr2 = [5, 4, 3, 2, 1]
print(check(arr1, arr2))  # Output: True

arr1 = [1, 2, 3, 4, 5]
arr2 = [5, 4, 3, 2, 6]
print(check(arr1, arr2))  # Output: False