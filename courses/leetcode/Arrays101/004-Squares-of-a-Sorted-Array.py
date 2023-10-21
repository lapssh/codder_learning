"""
Squares of a Sorted Array

Solution
Given an integer array nums sorted in non-decreasing order,
return an array of the squares of each number sorted in non-decreasing order.

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
"""
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted(x ** 2 for x in nums)


a = Solution()
input1 = [-4, -1, 0, 3, 10]
input2 = [-7, -3, 2, 3, 11]

print(a.sortedSquares(nums=input1))
print(a.sortedSquares(nums=input2))
