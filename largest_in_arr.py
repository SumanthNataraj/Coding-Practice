"""Largest Element in Array

Write a function to find the largest element in an array.
Given an array arr[]. The task is to find the largest element and return it."""

from typing import List


class Solution:
    def largest(self, arr : List[int]) -> int:
        # code here
        arr=sorted(arr)
        
        return arr[-1]
        



class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  #array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        arr = list(map(int, input().split()))

        obj = Solution()
        res = obj.largest(arr)

        print(res)
        print("~")