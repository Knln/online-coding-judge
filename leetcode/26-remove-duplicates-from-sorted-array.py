from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        previous = ''
        removed_num = 0

        for i, num in enumerate(list(nums)):
            if num == previous:
                nums.pop(i-removed_num)
                removed_num = removed_num + 1
            previous = num

        return i-removed_num+1

if __name__ == '__main__':
    solution = Solution()
    print("{}".format(solution.removeDuplicates([1,1,2])))
    print("{}".format(solution.removeDuplicates([0,1,2,2,3,3,4,4,4,4,4,5])))