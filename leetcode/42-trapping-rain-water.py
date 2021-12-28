from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:

        if not height:
            return 0

        left_max, right_max = [height[0]], [height[-1]]
        answer = 0

        for i in range(1, len(height)):
            left_max.append(max(left_max[i-1], height[i]))

        for i in range(2, len(height)+1):
            right_max.append(max(right_max[i-2], height[-i]))

        for i in range(1, len(height)-1):
            answer += min(left_max[i], right_max[-i-1]) - height[i]

        return answer

solution = Solution()
print(solution.trap(height=[0,1,0,2,1,0,1,3,2,1,2,1]))
print(solution.trap(height=[]))
print(solution.trap(height=[1]))
print(solution.trap(height=[0]))