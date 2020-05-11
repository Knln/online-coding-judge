# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

class doubleList:
    def __init__(self, val, next=None, before=None):
        self.val = val
        self.next = next
        self.before = before

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        carry = 0

        if l1 != None:
            newNode = doubleList(l1.val, None, None)
            head = newNode
            l1 = l1.next

        while l1 != None:
            newNode.next = doubleList(l1.val, next=None, before=newNode)
            newNode = newNode.next
            l1 = l1.next

        tempNode = head

        if l2 != None and tempNode != None:
            tempNum = tempNode.val + l2.val
            if tempNum > 9:
                tempNum = tempNum - 10
                carry = 1

            newNode = doubleList(tempNum, None, None)
            tempNode = tempNode.next
            l2 = l2.next

        head2 = newNode

        while (l2 != None) and (tempNode != None):
            tempNum = tempNode.val + l2.val + carry
            carry = 0
            if tempNum > 9:
                tempNum = tempNum - 10
                carry = 1

            newNode.next = doubleList(tempNum, None, before=newNode)
            newNode = newNode.next
            tempNode = tempNode.next
            l2 = l2.next

        if (l2 != None) and (tempNode == None):
            while l2 != None:
                tempNum = l2.val + carry
                carry = 0
                if tempNum > 9:
                    tempNum = tempNum - 10
                    carry = 1

                newNode.next = doubleList(tempNum, None, before=newNode)
                newNode = newNode.next
                l2 = l2.next

        elif (l2 == None) and (tempNode != None):
            while tempNode != None:
                tempNum = tempNode.val + carry
                carry = 0
                if tempNum > 9:
                    tempNum = tempNum - 10
                    carry = 1

                newNode.next = doubleList(tempNum, None, before=newNode)
                newNode = newNode.next
                tempNode = tempNode.next

        if carry == 1:
            newNode.next = doubleList(1, None, before=newNode)
            newNode = newNode.next

        return head2

if __name__ == "__main__":
    l1_1 = ListNode(3)
    l1_2 = ListNode(4, next=l1_1)
    l1_3 = ListNode(0, next=l1_2)
    l2_1 = ListNode(4)
    l2_2 = ListNode(6, next=l2_1)
    l2_3 = ListNode(5, next=l2_2)

    print("{}".format(Solution().addTwoNumbers(l1_3, l2_3)))
