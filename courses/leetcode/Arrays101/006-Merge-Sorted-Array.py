"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside
the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements
denote the elements that should be merged, and the last n elements are set to 0 and should
be ignored. nums2 has a length of n.

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
"""
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        print(f'{nums1=}, {nums2=}')
        for inx, item in enumerate(nums1):
            print(f'{inx=} - {item=}')
            if item == 0:
                if nums2:
                    nums1[inx] = nums2.pop()
        nums1.sort()
        # print(nums1)
        return nums1


a = Solution()
input1 = ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
input2 = ([1], 1, [], 0)
input3 = ([0], 0, [1], 1)
input4 = ([-1, 0, 0, 3, 3, 3, 0, 0, 0], 6, [1, 2, 2], 3)

print(a.merge(*input1))
print(a.merge(*input2))
print(a.merge(*input3))
print(a.merge(*input4))
