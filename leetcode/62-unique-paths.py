class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Base case
        if m <= 1 and n <= 1:
            return 1

        dp = [[0 for i in range(n)] for j in range(m)]
        dp[0][0] = 1

        for i in range(0, n):
            for j in range(0, m):
                if i == 0:
                    dp[j][i] = 1
                elif j == 0:
                    dp[j][i] = 1
                else:
                    dp[j][i] = dp[j][i-1] + dp[j-1][i]

        return dp[m-1][n-1]