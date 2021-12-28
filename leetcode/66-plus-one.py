from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        num_str = ''.join(str(digit) for digit in digits)
        answer = int(num_str) + 1

        if answer == 1 and len(num_str) > 1:
            digits[-1] = 1
            return digits


        return [int(x) for x in str(answer)]

solution = Solution()
print(solution.plusOne(digits=[1,2,3]))