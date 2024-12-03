"""
Missing in Array

You are given an array arr of size n - 1 that contains distinct integers in the range from 1 to n (inclusive). This array represents a permutation of the integers from 1 to n with one element missing. Your task is to identify and return the missing element.
"""

class Solution:
    
    # Note that the size of the array is n-1
    def missingNumber(self, n, arr):
        
        # Calculate the sum of all numbers from 1 to n
        e = n * (n + 1) // 2
        a=0
        # Calculate the sum of the given array
        for i in range(len(arr)):
            a+=arr[i]
            
        
        b=e-a
        
        return b
    
t = int(input())
for _ in range(0, t):
    arr = list(map(int, input().split()))
    s = Solution().missingNumber(arr)
    print(s)