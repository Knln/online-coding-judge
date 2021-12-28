from typing import List


class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:

        if not A:
            return 0

        count = 0
        sum = 0
        result = 0
        left, right = 0, 0

        for i, num in enumerate(A):
            sum += num

            if num == 1:
                count = 0

            while left <= i and sum >= S:
                if sum == S:
                    count += 1

                sum -= A[left]
                left += 1

            result += count

        return result

solution = Solution()
print(solution.numSubarraysWithSum(A=[1,0,1,0,1], S=2))
print(solution.numSubarraysWithSum(A=[0,0,0,0,0], S=0))