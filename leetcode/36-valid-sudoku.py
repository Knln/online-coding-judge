from typing import List
from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # (square, 1) : []
        # (row, 1) : []
        # (column, 1) : []

        dictionary = defaultdict(set)
        for i in range(1, len(board)):
            dictionary[("square", i)] = set()
            dictionary[("row", i)] = set()
            dictionary[("column", i)] = set()

        for r, rows in enumerate(board):
            for i, c in enumerate(rows):
                print((int(r) // 3) * 3 + (int(i) // 3 + 1))
                if c == ".":
                    continue

                if int(c) in dictionary["square", (int(r) // 3) * 3 + (int(i) // 3 + 1)] or int(c) in dictionary[("row", int(r)+1)] or int(c) in dictionary[("column", int(i)+1)]:
                    return False
                else:
                    dictionary["square", (int(r) // 3) * 3 + (int(i) // 3 + 1)].add(int(c))
                    dictionary[("row", int(r) + 1)].add(int(c))
                    dictionary[("column", int(i) + 1)].add(int(c))

        return True


solution = Solution()
print(solution.isValidSudoku(board=
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))