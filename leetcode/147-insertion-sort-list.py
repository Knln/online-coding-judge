# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:

        if not head or not head.next:
            return head

        perm_head, prev = head, head
        head = head.next

        while head:
            if prev.val > head.val:
                # Setting previous node to the next node
                prev.next = head.next
                save_head = head

                temp = perm_head
                temp_prev = perm_head

                while temp.val < head.val:
                    temp_prev = temp
                    temp = temp.next

                if temp == perm_head:
                    head.next = perm_head
                    perm_head = head
                else:
                    temp_prev.next = head
                    head.next = temp

                prev = save_head
                head = save_head.next
            else:
                prev = head
                head = head.next

        return perm_head


solution = Solution.insertionSortList()
