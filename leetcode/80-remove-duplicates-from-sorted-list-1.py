# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:

        original_head = head

        while head:
            while head.next and head.next.val == head.val:
                head.next = head.next.next
            head = head.next

        return original_head

def print_nodes(head: ListNode):
    while head:
        print(head.val)
        head = head.next

if __name__ == "__main__":

    node1 = ListNode(3)
    node2 = ListNode(2)
    node2.next = node1
    node3 = ListNode(2)
    node3.next = node2
    node4 = ListNode(1)
    node4.next = node3

    node5 = ListNode(3)
    node6 = ListNode(3)
    node6.next = node5
    node7 = ListNode(3)
    node7.next = node6

    solution = Solution()
    solution.deleteDuplicates(node4)
    solution.deleteDuplicates(node7)
    print_nodes(node4)
    print_nodes(node7)

