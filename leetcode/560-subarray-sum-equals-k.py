from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        map_of_values = {0: 0}
        count = 0
        sum = 0

        for num in nums:
            sum = num+sum

            if sum == k:
                count += 1

            if sum-k in map_of_values.keys():
                count += map_of_values[sum-k]

            if sum not in map_of_values.keys():
                map_of_values[sum] = 1
            else:
                map_of_values[sum] += 1

        return count


print(Solution().subarraySum([1,1,1], 2))
print(Solution().subarraySum([1,2,3], 3))
print(Solution().subarraySum([3,4,7,2,-3,1,4,2], 7))
print(Solution().subarraySum([-1], 0))