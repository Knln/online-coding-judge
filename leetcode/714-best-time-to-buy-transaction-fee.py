from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:

        if len(prices) < 2:
            return 0

        max_gain = [[None,None] for x in range(0, len(prices))]
        max_gain[0][0] = -prices[0]
        max_gain[0][1] = 0

        for i in range(1, len(prices)):
            # Between not buying stock before vs not buying stock now
            max_gain[i][0] = max(max_gain[i-1][0], max_gain[i-1][1] - prices[i])
            # Between selling stock now vs selling stock earlier
            max_gain[i][1] = max(max_gain[i-1][0]+prices[i]-fee, max_gain[i-1][1])

        print(max_gain)
        return max_gain[-1][1]

solution = Solution()
print(solution.maxProfit(prices=[1, 3, 2, 8, 4, 9], fee=2))