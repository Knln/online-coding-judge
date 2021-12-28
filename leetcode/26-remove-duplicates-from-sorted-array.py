from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        slow = ''
        deleted = 0
        last = len(nums)

        for i in range(0, last):
            if nums[i-deleted] == slow:
                del nums[i-deleted]
                deleted += 1

            slow = nums[i-deleted]

        return nums

if __name__ == '__main__':
    solution = Solution()
    print("{}".format(solution.removeDuplicates([1,1,2])))
    print("{}".format(solution.removeDuplicates([0,0,1,1,2,2,3,3,4,4,4,4,4,5])))