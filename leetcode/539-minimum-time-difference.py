from typing import List

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:

        floats = [int(x[0:2]) * int(60) + int(x[3:]) for x in timePoints]
        sorted_floats = sorted(floats)

        minimum = 1440
        day = 1440

        if len(sorted_floats) == 2:
            return min(day+sorted_floats[0]-sorted_floats[1], sorted_floats[1]-sorted_floats[0])

        for i in range(len(sorted_floats)):
            if i == len(sorted_floats)-1:
                minimum = min(day+sorted_floats[0]-sorted_floats[i], minimum)
            else:
                minimum = min(sorted_floats[i+1]-sorted_floats[i], minimum)

        return minimum


solution = Solution()
print(solution.findMinDifference(timePoints=["23:59","00:00"]))
print(solution.findMinDifference(timePoints=["00:00","23:59","00:00"]))