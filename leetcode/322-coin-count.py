class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        # Base Case
        if amount <= 0:
            return 0

        coins = sorted(coins)

        dp = [float('inf') for i in range(amount + 1)]

        for i in range(1, amount + 1):
            for c in coins:
                if i == c:
                    dp[i] = 1
                elif i > c:
                    dp[i] = min(dp[i], 1 + dp[i - c])
                else:
                    break
        if dp[amount] == float('inf'):
            return -1
        else:
            return int(dp[amount])