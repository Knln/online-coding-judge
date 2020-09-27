# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:

        visited = dict()

        while head:
            if head not in visited.keys():
                visited[head] = head.val
                head = head.next
            else:
                return True

        return False


if __name__ == "__main__":

    node1 = ListNode(3)
    node2 = ListNode(2)
    node2.next = node1
    node3 = ListNode(3)
    node3.next = node2
    node4 = ListNode(4)
    node4.next = node3
    node1.next = node4

    node5 = ListNode(3)
    node6 = ListNode(3)
    node6.next = node5
    node7 = ListNode(3)
    node7.next = node6

    solution = Solution()
    print(solution.hasCycle(node4))
    print(solution.hasCycle(node7))