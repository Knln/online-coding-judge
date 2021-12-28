from typing import List
from collections import defaultdict


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        visited = defaultdict(int)
        stack = []

        if target < matrix[0][0] or target > matrix[len(matrix)-1][len(matrix[0])-1]:
            return False

        i = 0
        for i, row in enumerate(matrix):
            if row[-1] >= target:
                break

        stack.append((i, 0))
        visited[(i, 0)] = 1

        while stack:

            m,n = stack.pop()
            print("({m},{n})".format(m=m, n=n))

            if matrix[m][n] == target:
                return True

            for coord in (m-1, n), (m, n+1), (m+1, n), (m, n-1):
                if 0 <= coord[0] < len(matrix) and 0 <= coord[1] < len(matrix[0]):
                    if coord not in visited:
                        if matrix[coord[0]][coord[1]] <= target:
                            visited[coord] = 1
                            stack.append(coord)
                    else:
                        continue

        return False


solution = Solution()
print(solution.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 21))