from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:

        def recursion(left, right, nums):
            if left > right:
                return None
            if left == right:
                return TreeNode(nums[left])
            else:
                mid = (left + right) // 2
                root = TreeNode(nums[mid])
                root.left = recursion(left, mid-1, nums)
                root.right = recursion(mid+1, right, nums)
                return root

        answer = recursion(0, len(nums)-1, nums)

        return answer

    @staticmethod
    def TreePrint(tree):
        if not tree:
            return

        print(tree.val)
        Solution.TreePrint(tree.left)
        Solution.TreePrint(tree.right)

solution = Solution()
tree = solution.sortedArrayToBST([-10,-3,0,5,9])
solution.TreePrint(tree)

        
