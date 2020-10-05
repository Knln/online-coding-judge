from typing import List

def searchInsert(nums: List[int], target: int) -> int:

    # Check for null case
    if not nums:
        return 0

    high = len(nums) - 1
    low = 0
    mid = 0

    while low <= high:
        mid = (high + low) // 2
        if nums[mid] < target:
            low = mid + 1
        elif nums[mid] > target:
            high = mid - 1
        else:
            # We have found the target
            return mid

    if low > high:
        return low
    else:
        return high


print(searchInsert([1,3,5,6], 5))
print(searchInsert([1,3,5,6], 7))
print(searchInsert([1,3,5,6], 0))
