from collections import Counter
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        for i in [k for k,v in Counter(nums).items() if v == 1]:
            return i

        return 0


if __name__ == "__main__":
    solution = Solution()
    print(solution.singleNumber([4, 1, 1]))
    print(solution.singleNumber([1, 0, 0, 1, 5]))
    print(solution.singleNumber([-1, -1, 5, 5, -4]))
    print(solution.singleNumber([999999999, 999999999, 999999998]))
