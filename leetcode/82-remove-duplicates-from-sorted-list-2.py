# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:

        dummy_node = ListNode(next=head)
        saved_node = dummy_node
        counter = 0

        while head:
            while head.next and head.next.val == head.val:
                head.next = head.next.next
                counter = 1
            if counter == 1:
                head = saved_node
                head.next = head.next.next
                counter = 0
            else:
                saved_node = head

            head = head.next

        return dummy_node.next

def print_nodes(head: ListNode):
    while head:
        print(head.val)
        head = head.next


if __name__ == "__main__":

    node0 = ListNode(3)
    node1 = ListNode(2)
    node1.next = node0
    node2 = ListNode(1)
    node2.next = node1
    node3 = ListNode(1)
    node3.next = node2
    node4 = ListNode(1)
    node4.next = node3

    node5 = ListNode(3)
    node6 = ListNode(3)
    node6.next = node5
    node7 = ListNode(3)
    node7.next = node6

    solution = Solution()
    print_nodes(solution.deleteDuplicates(node4))
    print_nodes(solution.deleteDuplicates(node7))