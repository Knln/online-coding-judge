from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        count = 0

        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if int(grid[i][j]) == 1:
                    count += 1
                    self.dfs(grid, i, j)

        return count

    def dfs(self, grid, i, j):

        stack = []
        stack.append((i,j))

        while stack:
            coord = stack.pop()

            if int(grid[coord[0]][coord[1]]) != 1:
                continue

            grid[coord[0]][coord[1]] = 0

            c_array = []

            c_array.append((coord[0]-1, coord[1]))
            c_array.append((coord[0]+1, coord[1]))
            c_array.append((coord[0], coord[1]-1))
            c_array.append((coord[0], coord[1]+1))

            for node in c_array:
                if 0 <= node[0] < len(grid) and 0 <= node[1] < len(grid[0]):
                    stack.append(node)


solution = Solution()

print(solution.numIslands(grid = [
  ["1","1","0","0","1"],
  ["1","1","0","1","1"],
  ["0","0","1","1","0"],
  ["0","1","0","1","1"]
]))
