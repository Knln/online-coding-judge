from collections import defaultdict


class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]

        if not target:
            return ""

        dictionary = defaultdict(tuple)
        answer = ""

        for i, row in enumerate(board):
            row = [x for x in row]
            for j, column in enumerate(row):
                dictionary[column] = (i, j)

        for i in range(len(target)):
            if i == 0:
                temp = (0 - dictionary[target[i]][0], 0 - dictionary[target[i]][1])
            else:
                temp = (dictionary[target[i-1]][0] - dictionary[target[i]][0], dictionary[target[i-1]][1] - dictionary[target[i]][1])

            if target[i-1] == "z":
                if temp[0] < 0:
                    answer += -1 * temp[0] * "D"
                elif temp[0] > 0:
                    answer += temp[0] * "U"

                if temp[1] < 0:
                    answer += -1 * temp[1] * "R"
                elif temp[1] > 0:
                    answer += temp[1] * "L"
            else:
                if temp[1] < 0:
                    answer += -1 * temp[1] * "R"
                elif temp[1] > 0:
                    answer += temp[1] * "L"

                if temp[0] < 0:
                    answer += -1 * temp[0] * "D"
                elif temp[0] > 0:
                    answer += temp[0] * "U"

            answer += "!"

        return answer


solution = Solution()
print(solution.alphabetBoardPath(target="zdz"))
print(solution.alphabetBoardPath(target="code"))