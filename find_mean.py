def findMean(arr):
    
    if(len(arr)<=2):
        return -1
    small=arr[0]
    large=arr[0]
    n=len(arr)
    for num in arr:
        if num<small:
            small=num
        if num>large:
            large=num
            
    rem_elements=[num for num in arr if num<large and num>small]
    mean=sum(rem_elements)/(n-2)
    return mean

arr=[0,1,2,3,4,5,6,7]
print(findMean(arr))
print("--------------------------")
arr1=[]

print(findMean(arr1))