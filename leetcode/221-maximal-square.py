from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:


        m = len(matrix)
        n = len(matrix[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]

        if int(matrix[0][0]) == 0:
            dp[0][0] = 0
        else:
            dp[0][0] = 1

        maximum_number = dp[0][0]

        for i in range(m):
            for j in range(n):
                if j == 0 and i == 0:
                    continue

                if int(matrix[i][j]) == 1:
                    dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1
                    maximum_number = max(maximum_number, dp[i][j])
                else:
                    continue

        if maximum_number == 0:
            return 0
        else:
            return pow(maximum_number, 2)

solution = Solution()
print(solution.maximalSquare(matrix=[["0"]]))