"""Given a sorted array arr. Return the size of the modified array which contains only distinct elements.
Note:
1. Don't use set or HashMap to solve the problem.
2. You must return the modified array size only where distinct elements are present and modify the original array such that all the distinct elements come at the beginning of the original array."""



def remove_duplicate( arr):
    
    l = []
    i = 0
    for j in range(i+1,len(arr)):
        if arr[i] != arr[j]:
            i+=1
            arr[i] = arr[j]
    return i+1


    
arr = [ 1 , 2 , 3 , 4 , 1 , 2 , 3 , 4 , 5 ]
    
ans = remove_duplicate(arr)
for i in range(ans):
    print(ans[i], end=" ")
    print()
    print("~")

