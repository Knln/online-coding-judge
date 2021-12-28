from typing import List

def intersection(nums1: List[int], nums2: List[int]) -> List[int]:

    intersection_dict = dict()
    intersection_list = list()

    for num in nums1:
        if num not in intersection_dict:
            intersection_dict[num] = 1

    for num in nums2:
        if num in intersection_dict:
            intersection_dict[num] += 1

    for k, v in intersection_dict.items():
        if v > 1:
            intersection_list.append(k)

    return intersection_list

print(intersection([1,2,2,1],[2,2]))
print(intersection([4,9,5],[9,4,9,8,4]))