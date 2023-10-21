"""
Given an array nums of integers, return how many of them contain an even number of digits.
Input: nums = [12,345,2,6,7896]
Output: 2
Explanation:
12 contains 2 digits (even number of digits).
345 contains 3 digits (odd number of digits).
2 contains 1 digit (odd number of digits).
6 contains 1 digit (odd number of digits).
7896 contains 4 digits (even number of digits).
Therefore only 12 and 7896 contain an even number of digits.
"""
from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        cnt = 0
        for num in nums:
            # print(len(str(num)) % 2)
            if len(str(num)) % 2 == 0:
                cnt += 1
        return cnt


input1 = [12, 345, 2, 6, 7896]
input2 = [555, 901, 482, 1771]
a = Solution()
print(a.findNumbers(input1))
print(a.findNumbers(input2))
