from typing import List
from math import sqrt


class Solution:

    def findPythagoras(self, list):

        sum = 0
        for number in list:
            sum = int(number)**2 + sum

        return sqrt(sum)

    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:

        longest_point_dictionary = dict()
        answer = list()

        if len(points) == 1:
            return points

        for idx, point in enumerate(points):
            summation = self.findPythagoras(point)
            longest_point_dictionary[tuple(point)] = summation

        ordered_list = sorted(longest_point_dictionary.items(), key=lambda x:x[1])
        for i in range(0, K):
            answer.append(list(ordered_list[i][0]))

        return answer


if __name__ == "__main__":
    solution = Solution()
    print("{}".format(solution.kClosest([[0,1], [1,0], [3,2], [2,5]], 2)))
