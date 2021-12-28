# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        prev = None

        while head:
            n = head.next
            head.next = prev
            prev = head
            head = n

        return prev

    def reverseListRecursive(self, head: ListNode, prev=None) -> ListNode:
        if not head:
            return prev

        n = head.next
        head.next = prev
        return self.reverseListRecursive(n, head)


def print_nodes(head: ListNode):
    while head:
        print(head.val)
        head = head.next


if __name__ == "__main__":
    l2_1 = ListNode(4)
    l2_2 = ListNode(6, next=l2_1)
    l2_3 = ListNode(5, next=l2_2)

    print("{}".format(print_nodes(Solution().reverseListRecursive(l2_3))))