from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:

        i, j = 0, 0

        while i < len(nums):
            if nums[i] != 0 and i != j:
                if nums[j] == 0:
                    tmp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = tmp
                    j += 1
                    i += 1
                else:
                    j += 1
            elif nums[i] != 0 and i == j:
                i += 1
                j += 1
            else:
                i += 1

        return None


if __name__ == "__main__":
    solution = Solution()
    print(solution.moveZeroes([4, 1, 1]))
    print(solution.moveZeroes([0, 0, 0, 1, 5]))
    print(solution.moveZeroes([-1, 0, 0, 0, -4]))
    print(solution.moveZeroes([-1, 0, 1, 2, 0]))
    print(solution.moveZeroes([4, 0, 1, 0]))
    print(solution.moveZeroes([4, 0, 0, 2, 1, 0, 5, 0, 0, 6, -1, 0]))
    print(solution.moveZeroes([0]))
    print(solution.moveZeroes([-111]))
