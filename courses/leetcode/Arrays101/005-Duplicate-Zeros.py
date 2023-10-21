"""
 Duplicate Zeros

Solution
Given a fixed-length integer array arr, duplicate each occurrence of zero,
shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written.
Do the above modifications to the input array in place and do not return anything.

Example 1:

Input: arr = [1,0,2,3,0,4,5,0]
Output: [1,0,0,2,3,0,0,4]
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
"""
from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        flag = False
        for inx, item in enumerate(arr):
            if flag == True:
                flag = False
                continue
            if item == 0:
                arr.insert(inx,0)
                arr.pop()
                flag = True
                print(arr)



a = Solution()
nums1 = [1, 0, 2, 3, 0, 4, 5, 0]
print(a.duplicateZeros(nums1))
