from typing import List


class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:

        count = 0
        left, right = 0, 0

        while left < len(A):
            temp = dict()
            temp[A[left]] = 1
            while right < len(A):
                if right - left + 1 < K:
                    temp[A[right]] = 1
                    right += 1
                    continue
                else:
                    print(temp)
                    print(right)
                    print(len(temp))
                    if len(temp) < K:
                        temp[A[right]] = 1
                    elif len(temp) == K:
                        if A[right] in temp.keys():
                            count += 1
                        else:
                            count += 1
                            break
                    else:
                        break

                    right += 1

            left += 1

        return count

solution = Solution()
print(solution.subarraysWithKDistinct( A = [1,2,1,3,4], K = 3))