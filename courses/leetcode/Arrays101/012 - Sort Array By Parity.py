'''
Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.

Example 1:
Input: nums = [3,1,2,4]
Output: [2,4,3,1]
Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

Example 2:
Input: nums = [0]
Output: [0]
'''
from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        is_even = lambda x: x % 2 == 0
        idx = 0
        for i in range(0, len(nums)):
            if is_even(nums[idx]):
                idx += 1
                continue
            else:
                tmp = nums.pop(idx)
                nums.append(tmp)
            if is_even(nums[idx]):
                idx += 1
        return nums


a = Solution()
# nums = [3, 1, 2, 4]
# nums = [0]
nums = [0, 1, 2]  # [0,2,1]
print(a.sortArrayByParity(nums))
