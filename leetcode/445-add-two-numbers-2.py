from collections import deque
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        number_1 = 0
        number_2 = 0
        solution = 0

        while l1:
            number_1 = number_1 * 10
            number_1 = number_1 + l1.val
            l1 = l1.next

        while l2:
            number_2 = number_2 * 10
            number_2 = number_2 + l2.val
            l2 = l2.next

        solution = number_1 + number_2

        head = ListNode(0)
        if solution == 0:
            return head

        while solution > 0:
            x, solution = solution % 10, solution // 10
            head.next, head.next.next = ListNode(int(x)), head.next

        return head.next

def print_nodes(head: ListNode):
    while head:
        print(head.val)
        head = head.next

if __name__ == "__main__":

    l1_3 = ListNode(0)
    l2_5 = ListNode(100)

    print_nodes(Solution().addTwoNumbers(l1_3, l2_5))