"""
remove (multiple) min value from a linked-list in one scan
"""
class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

def removeMinNodes(head):
    dummy = ListNode(float('INF'))
    dummy.next = ListNode(float('INF'))

    p = dummy
    while head:
        if head.val <=  p.next.val:
            p.next.next = head
            head = head.next
        else:
            temp = head.next
            head.next = p.next
            p.next = head
            head = temp
        p = p.next
    p.next= None
    return dummy.next.next



