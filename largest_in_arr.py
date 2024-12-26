"""Largest Element in Array

Write a function to find the largest element in an array.
Given an array arr[]. The task is to find the largest element and return it."""

from typing import List



def largest(arr : List[int]) -> int:
    # code here
    arr=sorted(arr)
    return arr[-1]

# Test the function

arr = [5, 2, 8, 1, 3, 6, 4]
print(largest(arr)) # Output: 8

arr = [-10, -20, -30, -40, -50]

print(largest(arr)) # Output: -10
        

