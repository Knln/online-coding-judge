class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        maximum_gain = 0
        cheapest = prices[0]

        for i in range(1, len(prices)):
            if cheapest > prices[i]:
                cheapest = prices[i]
            if maximum_gain < prices[i]:
                maximum_gain = max(maximum_gain, prices[i] - cheapest)

        return maximum_gain