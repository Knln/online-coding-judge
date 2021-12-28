from collections import defaultdict


class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:

        directions = [(-1,-2), (-2,-1), (-2,1), (-1, 2), (1,-2), (1, 2), (2, -1), (2, 1)]
        squares = defaultdict()
        iterations = 0
        denominator = pow(8, K)

        squares[(r,c)] = 1

        while iterations < K:
            iterations += 1
            new_squares = squares.copy()
            for k in new_squares.keys():
                count = squares[k]
                for element in directions:
                    if 0 <= k[0]+element[0] < N and 0 <= k[1]+element[1] < N:
                        if (k[0]+element[0], k[1]+element[1]) in squares:
                            squares[(k[0]+element[0], k[1]+element[1])] += count
                        else:
                            squares[(k[0] + element[0], k[1] + element[1])] = count

                squares.pop(k)

        answer = sum(squares.values())/denominator

        return answer


solution = Solution()
print(solution.knightProbability(3,3,0,0))