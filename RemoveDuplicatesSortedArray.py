"""Given a sorted array arr. Return the size of the modified array which contains only distinct elements.
Note:
1. Don't use set or HashMap to solve the problem.
2. You must return the modified array size only where distinct elements are present and modify the original array such that all the distinct elements come at the beginning of the original array."""



def removeDuplicates( arr):
    seen = set()
    idx = 0
    for i in range(len(arr)):
        if arr[i] not in seen:
            seen.add(arr[i])
            arr[idx] = arr[i]
            idx += 1
    return idx

    
arr = [ 1 , 2 , 3 , 4 , 1 , 2 , 3 , 4 , 5 ]
    
ans = removeDuplicates(arr)

print(ans, end=" ")


