def selectionsort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        
if __name__ == "__main__":
    
    arr = [64, 25, 12, 22, 11]
    print("Unsorted array:")
    for i in range(len(arr)):
        print("%d" % arr[i], end=" ")
    
    selectionsort(arr)
    
    print("\nSorted array:")
    for i in range(len(arr)):
        print("%d" % arr[i], end=" ")
        