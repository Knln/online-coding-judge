from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers)-1

        while i < j:
            if numbers[i] + numbers[j] == target:
                return [i+1, j+1]
            elif numbers[i] + numbers[j] < target:
                i += 1
            else:
                j -= 1


if __name__ == "__main__":
    solution = Solution()
    print("{}".format(solution.twoSum([0, 7, 11, 15, 15, 28], 30)))
