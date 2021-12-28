from collections import defaultdict
from typing import List

# Adds keys : values to list where key is the input and values
# is the target - key. If we manage to find the collorary eg. 30 - 10 = 30 - 20
# then we found our answer!
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        solutionList = defaultdict(int)
        indexList = []

        # O(n) time
        for count, n in enumerate(nums):
            result = target - n
            if result in solutionList.keys():
                indexList.append(nums.index(result))
                indexList.append(count)
                return indexList
            solutionList[n] = result

        return indexList


if __name__ == "__main__":
    print('{}'.format(Solution().twoSum([0, 7, 11, 15, 15, 0], 0)))
