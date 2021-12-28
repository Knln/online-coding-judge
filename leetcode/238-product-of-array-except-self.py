from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        new_array = []
        zeroes = {0: 0}
        product = 1

        for i in range(len(nums)):
            if nums[i] == 0:
                zeroes[0] += 1
                continue

            if zeroes[0] > 1:
                product = 0
                break

            product *= nums[i]

        for j in range(len(nums)):
            if zeroes[0] > 1:
                new_array.append(0)
            elif zeroes[0] == 1:
                if nums[j] == 0:
                    new_array.append(product)
                else:
                    new_array.append(0)
            else:
                new_array.append(int(product / nums[j]))

        return new_array

solution = Solution()
print(solution.productExceptSelf([1,2,3,4]))
print(solution.productExceptSelf([1,2,0,3,-3]))