from typing import List

def lengthOfLIS(nums: List[int]) -> int:

    # Base Case
    if not nums:
        return 0

    longest = [1 for i in range(len(nums))]
    answer = 0

    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                longest[i] = max(longest[i], longest[j]+1)
        answer = max(longest[i], answer)

    return answer

print(lengthOfLIS([1,3,6,7,9,4,10,5,6]))