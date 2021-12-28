class Solution:
    def climbStairs(self, n: int) -> int:

        if n == 1:
            return 1

        if n == 2:
            return 2

        f_n1 = 2
        f_n2 = 1
        answer = 0

        for i in range(3, n+1):
            answer = f_n1 + f_n2
            f_n2 = f_n1
            f_n1 = answer

        return answer

solution = Solution()
print(solution.climbStairs(3))