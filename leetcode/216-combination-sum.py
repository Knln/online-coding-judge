from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        maximum = 1+2+3+4+5+6+7+8+9
        if n > maximum:
            return []

        answer = []

        def helper(k, n, num, arr, answer):
            #print(arr)

            if len(arr) == k and sum(arr) == n:
                if arr not in answer:
                    answer.append(list(arr))
                return

            if len(arr) > k or num > 9:
                return

            if n >= 10:
                max_num = 10
            else:
                max_num = n+1

            for i in range(num, max_num):
                arr.append(i)
                helper(k, n, i+1, arr, answer)
                arr.pop()

        helper(k, n, 1, [], answer)

        return answer

solution = Solution()
#print(solution.combinationSum3(k=3, n=7))
print(solution.combinationSum3(k=9, n=45))
#print(solution.combinationSum3(k=4, n=1))