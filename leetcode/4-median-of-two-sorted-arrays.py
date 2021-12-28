from typing import List
'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]
The median is 2.0
'''


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        both_nums = nums1 + nums2
        both_nums.sort()
        length = len(both_nums)
        if length == 0:
            result = 0
        elif length % 2 == 0:
            upper_median = both_nums[int(length/2)]
            lower_median = both_nums[int((length-1)/2)]
            result = float((upper_median+lower_median)/2)
        else:
            result = float(both_nums[int((length-1)/2)])

        return result


if __name__ == '__main__':
    solution = Solution()
    print("{}".format(solution.findMedianSortedArrays([1, 2, 3], [4, 5, 6])))