class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:

        counter = Counter(nums)
        new_nums = sorted([x for x in counter.keys()])

        dp = [0 for x in range(len(new_nums))]
        dp2 = [0 for x in range(len(new_nums))]

        maximum = 0

        print(counter)

        for i in range(0, len(new_nums)):

            if new_nums[i - 1] == new_nums[i] - 1:

                dp[i] = max(new_nums[i] * counter[new_nums[i]] + dp[i - 2], dp[i - 1])
            else:
                dp[i] = dp[i - 1] + new_nums[i] * counter[new_nums[i]]

            maximum = max(dp[i], maximum)

        return maximum