from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        dp1 = [[float('inf') for _ in range(len(grid[0]))] for _ in range(len(grid))]

        dp1[0][0] = grid[0][0]

        for i in range(len(grid)):
            for j in range(len(grid[0])):

                if i > 0 and j > 0:
                    dp1[i][j] = min(dp1[i-1][j]+grid[i][j], dp1[i][j-1]+grid[i][j])
                elif i == 0 and j != 0:
                    dp1[i][j] = dp1[i][j-1] + grid[i][j]
                elif j == 0 and i != 0:
                    dp1[i][j] = dp1[i-1][j] + grid[i][j]
                else:
                    continue

        return int(dp1[len(grid)-1][len(grid[0])-1])


solution = Solution()
print(solution.minPathSum([[1,3,1,2],[1,5,1,3],[4,2,1,5]]))
