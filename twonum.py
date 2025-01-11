def two_num(arr,target):
    
    n= len(arr)
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]+arr[j]== target:
                return i,j
        
    return -1,-1

arr=[1,2,3,4,5]

#arr=[5,4,3,8,2,78,4]
#arr=[]

print(two_num(arr,10))