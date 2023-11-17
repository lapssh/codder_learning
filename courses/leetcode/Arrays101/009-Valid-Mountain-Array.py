'''
Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

Example 1:
Input: arr = [2,1]
Output: false

Example 2:
Input: arr = [3,5,5]
Output: false

Example 3:
Input: arr = [0,3,2,1]
Output: true
'''
from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        last = arr[-1]
        # ищем вершину
        print(f'Массив: {arr}')
        pik = max(arr)
        if arr.count(pik) > 1:
            return False
        print('Пик: ', pik)
        left = arr[:arr.index(pik)]
        right = arr[arr.index(pik) + 1:]
        if left == [] or right == []:
            print('пусто')
            return False
        print(f'{left=}    {right=}')
        last = left[0]
        for i in left[1:]:
            if i <= last:
                return False
            last = i
        last = right[0]
        for i in right[1:]:
            if i >= last:
                return False
            last = i
        return True


# arr = [0, 3, 2, 1]
# arr = [0, 2, 3, 4, 5, 2, 1, 0]
# arr = [0, 2, 3, 9, 5, 6, 1, 0]
arr = [2, 1]
a = Solution()
print(a.validMountainArray(arr))
