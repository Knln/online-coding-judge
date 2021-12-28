from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        maxArea = 0

        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == 1:
                    maxArea = max(self.dfs(grid, i, j), maxArea)

        return maxArea

    def dfs(self, grid, i, j):

        stack = [(i, j)]
        count = 0

        while stack:
            coord = stack.pop()

            if int(grid[coord[0]][coord[1]]) != 1:
                continue

            count += 1

            grid[coord[0]][coord[1]] = 0

            c_array = [(coord[0] - 1, coord[1]), (coord[0] + 1, coord[1]), (coord[0], coord[1] - 1),
                       (coord[0], coord[1] + 1)]

            for node in c_array:
                if 0 <= node[0] < len(grid) and 0 <= node[1] < len(grid[0]):
                    stack.append(node)

        return count

solution = Solution()

print(solution.maxAreaOfIsland(grid=[[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]]
))
