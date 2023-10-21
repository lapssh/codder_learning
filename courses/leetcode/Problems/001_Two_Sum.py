"""
Given an array of integers nums and an integer target, return indices of the two numbers such that
 they add up to target.

You may assume that each input would have exactly one solution,
 and you may not use the same element twice.

You can return the answer in any order.
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_num1 = 0
        index_num2 = 1
        while True:
            num1, nums = nums[0], nums[1:]
            for num2 in nums:
                if num1 + num2 == target:
                    return [index_num1, index_num2]
                index_num2 += 1
            index_num1 += 1
            index_num2 = index_num1 + 1



a = Solution()
print(a.twoSum(nums=[2, 7, 11, 15], target=9))
print(a.twoSum(nums=[3, 2, 4], target=6))
print(a.twoSum(nums=[3, 3], target=6))
print(a.twoSum(nums=[2, 5, 5, 11], target=10))

# BEST
"""
Solution 3: (One-pass Hash Table)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        n = len(nums)

        for i in range(n):
            complement = target - nums[i]
            if complement in numMap:
                return [numMap[complement], i]
            numMap[nums[i]] = i

        return []  # No solution found
"""