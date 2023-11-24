'''
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers
in the range [1, n] that do not appear in nums.

Example 1:
Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]

Example 2:
Input: nums = [1,1]
Output: [2]
'''
from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        scope = list(range(1, len(nums)+1))
        result = set(scope) - set(nums)
        return list(result)


nums = [4, 3, 2, 7, 8, 2, 3, 1]
# nums = [1, 1]
# nums = [2, 2]
# nums = [1,1,2,2]
a = Solution()
print(a.findDisappearedNumbers(nums))
