from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_lenght = 0
        results = []
        for num in nums:
            print(f'{num=}')
            if num == 1:
                max_lenght += 1
            elif num == 0:
                # results.append(max_lenght)
                max_lenght = 0
            results.append(max_lenght)
            print(results)
        return max(results)
        # print(results)


nums = [1, 1, 0, 1, 1, 1]
nums2 = [1, 0, 1, 1, 0, 1]
nums3 = [1, 1, 0, 1, 1, 1]
a = Solution()
# answer = a.findMaxConsecutiveOnes(nums=nums)
#
# print('input:', nums, '\n', 'Output:', answer)
# answer = a.findMaxConsecutiveOnes(nums=nums2)
# print('input:', nums2, '\n', 'Output:', answer)

answer = a.findMaxConsecutiveOnes(nums=nums3)
print('input:', nums3, '\n', 'Output:', answer)
