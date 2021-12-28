from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        if len(nums) == 1:
            return nums[0]

        ans = curr = nums[0]
        for i in range(len(nums)):
            curr = max(nums[i], nums[i]+curr)
            ans = max(ans, curr)

        return ans


if __name__ == "__main__":
    solution = Solution()
    print("{}".format(solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])))