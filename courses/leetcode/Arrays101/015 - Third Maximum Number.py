'''
Given an integer array nums, return the third distinct maximum number in this array.
If the third maximum does not exist, return the maximum number.

Example 1:
Input: nums = [3,2,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2.
The third distinct maximum is 1.

Example 2:
Input: nums = [1,2]
Output: 2
Explanation:
The first distinct maximum is 2.
The second distinct maximum is 1.
The third distinct maximum does not exist, so the maximum (2) is returned instead.

Example 3:
Input: nums = [2,2,3,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2 (both 2's are counted together since they have the same value).
The third distinct maximum is 1.
'''
from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = set(nums)
        nums2 = list(sorted(nums))
        if len(nums2) >= 3: return nums2[-3]
        if len(nums2) == 2:
            return nums2[-1]
        if len(nums2) == 1:
            return nums2[-1]


nums = [2, 2, 3, 1]
# nums = [1, 2]
# nums = [1, 2, 3, 4, 5]
# nums = [3, 2, 1]
a = Solution()
print(a.thirdMax(nums))
