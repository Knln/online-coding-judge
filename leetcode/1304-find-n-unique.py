from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:

        answer = []

        if n % 2 != 0:
            answer.append(0)

        for i in range(1, n // 2 + 1):
            answer.append(i)
            answer.append(-i)

        return answer

solution = Solution()
print(solution.sumZero(5))
print(solution.sumZero(4))
print(solution.sumZero(3))
print(solution.sumZero(1))