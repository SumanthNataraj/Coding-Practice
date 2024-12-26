"""Given a sorted array arr[] of distinct integers. Sort the array into a wave-like array(In Place). In other words, arrange the elements into a sequence such that arr[1] >= arr[2] <= arr[3] >= arr[4] <= arr[5].....
If there are multiple solutions, find the lexicographically smallest one.
Note: The given array is sorted in ascending order, and you don't need to return anything to change the original array."""

def convertToWave(n : int, arr : list[int]) -> None:
        
        # Convert the array into a wave-like array
        # Swap adjacent elements if they are not in the correct order
        # This process will ensure that the array is sorted in wave-like form
        temp=0
        for i in range(0,int(len(arr)-1),2):
            arr[i],arr[i+1]=arr[i+1],arr[i]
            
        return arr

# Test the function with an example 
                   
arr = [1, 2, 3, 4, 5]
convertToWave(arr, len(arr))
print(arr)  # Output: [2, 1, 4, 3, 5]
