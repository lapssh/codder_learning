"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted,
you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val.
The remaining elements of nums are not important as well as the size of nums.
Return k.
"""
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        cnt = 0
        for inx, el in enumerate(nums):
            if el == val:
                nums[inx] = 200
                cnt += 1
        nums.sort()
        print(f'{nums=}  {cnt=} {len(nums)-cnt=}')
        return len(nums) - cnt


nums = [3, 2, 2, 3]
val = 3
result01 = Solution()
assert result01.removeElement(nums, val) == 2, 'первая провалена'
nums = [3, 2, 2, 3]
result02 = Solution()
print('Результат: ', result02.removeElement(nums, val))
