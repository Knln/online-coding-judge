from typing import List
from collections import defaultdict

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:

        T.reverse()
        answer = [0 for _ in range(len(T))]

        for i in range(1, len(T)):
            for j in range(i-1, -1, -1):
                if T[j] > T[i]:
                    answer[-i-1] = i-j
                    break

        return answer


solution = Solution()
print(solution.dailyTemperatures(T = [73, 74, 75, 71, 69, 72, 76, 73]))