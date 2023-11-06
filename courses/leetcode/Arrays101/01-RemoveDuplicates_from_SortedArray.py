from typing import List


def removeDuplicates(nums: List[int]) -> int:
    # return len(nums) = list(set(nums))
    index = 0
    while True:
        try:
            next = nums[index+1]
            print(f"Шаг {index}")
            print(nums[index], nums[next])
            if next == nums[index]:
                nums.pop(index+1)
                continue
            index += 1
        except:
            break
    return len(nums)


nums1 = [1, 1, 2]
nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

answer1 = removeDuplicates(nums1)
answer2 = removeDuplicates(nums2)

print(f"{answer1=}")
print(f"{answer2=}")
