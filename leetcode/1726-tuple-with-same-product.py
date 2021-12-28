from typing import List
from collections import defaultdict

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:

        store = defaultdict(list)

        duplicates = set()
        answer = 0

        for i, num in enumerate(nums):
            j = i+1
            while j < len(nums):
                if store[num * nums[j]]:
                    duplicates.add(num * nums[j])
                store[num * nums[j]].append((num, nums[j]))

                j += 1

        for d in duplicates:
            combo = len(store[d])
            print( combo * (combo-1)//2 * 8)
            answer += combo * (combo-1)//2 * 8

        return int(answer)

solution = Solution()
print(solution.tupleSameProduct(nums = [2,3,4,6]))
print(solution.tupleSameProduct(nums = [2,3,4,6,8,12]))
print(solution.tupleSameProduct(nums = [1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192]))

