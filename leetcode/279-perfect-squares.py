import math


class Solution:
    def numSquares(self, n: int) -> int:

        squares = []
        dp = [float('inf') for x in range(n+1)]
        dp[0] = float('inf')

        for i in range(1, n+1):
            if math.sqrt(i).is_integer():
                squares.append(i)
                dp[i] = 1
            else:
                for s in squares:
                    if s < i:
                        dp[i] = min(1 + dp[i-1], dp[s] + dp[i-s], dp[i])
                    elif s == i:
                        dp[i] = 1
                    else:
                        continue

        return int(dp[n])

solution = Solution()
print(solution.numSquares(1))
print(solution.numSquares(13))