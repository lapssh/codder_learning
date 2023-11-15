'''
008-Chek-if-N-and-its-Double-Exist
Given an array arr of integers, check if there exist two indices i and j such that :
i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]

Example 1:
Input: arr = [10,2,5,3]
Output: true
Explanation: For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]
'''
from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        if (arr.count(0) >= 2):
            return True
        for i in range(len(arr) - 1):
            for j in range(i + 1, len(arr)):
                if arr[j] != 0 and arr[i] != 0:
                    if arr[i] / arr[j] == 2 or arr[j] / arr[i] == 2:
                        return True
        return False


# arr = [10, 2, 5, 3]
# arr = [3, 1, 7, 11]
arr = [-2, 0, 10, -19, 4, 6, -8]  # False
# arr = [-10, 12, -20, -8, 15]
# arr = [0, 0] # True
# arr = [-2, 0, 10, -19, 4, 6, -8]
# arr = [0, 0, 0, 0, 0]  # True
a = Solution()
print(a.checkIfExist(arr))
