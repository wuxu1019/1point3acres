"""
Given a non-negative integer represented as non-empty a singly linked list of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.

Example:
Input:
1->2->3

Output:
1->2->4

"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def plusOne_twopass(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        data = []
        while head:
            data.append(head.val)
            head = head.next
        carry = 1
        for i in range(len(data)-1, -1, -1):
            if data[i] + carry == 10:
                carry = 1
                data[i] = 0
            else:
                data[i] = data[i] + carry
                carry = 0
                break
        dummy = p = ListNode(0)
        if carry:
            p.next = ListNode(1)
            p = p.next
        for i in range(len(data)):
            p.next = ListNode(data[i])
            p = p.next
        return dummy.next

    def plusOne_onepass(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = head
        start = None
        while p:
            if p.val < 9:
                start = p
            p = p.next

        if start:
            start.val += 1
            change = start.next
        else:
            new = ListNode(1)
            new.next = head
            head = new
            change = head.next

        while change:
            change.val = 0
            change = change.next

        return head