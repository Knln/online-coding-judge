from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        early, late = newInterval[0], newInterval[1]

        new_array = []
        raise_flag = 0

        if not intervals:
            return [newInterval]

        if early < intervals[0][0]:
            start = early
            raise_flag = 1
        else:
            start = early

        # if early is l0, l1, or between l0 and l1
        for i, l in enumerate(intervals):
            if l[0] <= early <= l[1] and not l[0] <= late <= l[1]:
                raise_flag = 1
                start = l[0]
            elif l[0] <= early <= l[1] and l[0] <= late <= l[1]:
                new_array.append(l)
            elif i != len(intervals)-1 and l[1] < early < intervals[i+1][0]:
                start = early
                raise_flag = 1
                new_array.append(l)
            elif raise_flag == 1 and l[0] <= late <= l[1]:
                new_array.append([start, l[1]])
                raise_flag = 0
            elif raise_flag == 1 and late < l[0]:
                new_array.append([start, late])
                new_array.append(l)
                raise_flag = 0
            elif raise_flag == 1 and late > l[1]:
                continue
            else:
                new_array.append(l)

        if late > intervals[-1][1]:
            new_array.append([start, late])

        return new_array

solution = Solution()
print(solution.insert(intervals=[[1,3],[6,9]], newInterval = [2,5]))
print(solution.insert(intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]))
print(solution.insert(intervals = [], newInterval = [5,7]))
print(solution.insert(intervals = [[1,5]], newInterval = [2,3]))
print(solution.insert(intervals = [[1,5]], newInterval = [2,7]))
print(solution.insert(intervals = [[1,5]], newInterval = [6,8]))
print(solution.insert(intervals = [[1,5]], newInterval = [0,3]))
print(solution.insert(intervals = [[0,5],[9,12]], newInterval = [7,16]))
print(solution.insert(intervals = [[1,3],[6,8],[9,9]], newInterval = [7,8]))

