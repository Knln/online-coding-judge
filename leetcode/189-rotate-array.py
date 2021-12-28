from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        right = len(nums) - k
        print(nums[:right-1:-1])
        nums = nums[:right-1:-1] + nums[:right]
        print(nums)



if __name__ == "__main__":
    solution = Solution()
    solution.rotate([0, 1, 2, 5, -99, 10000], 2)
