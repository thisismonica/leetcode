# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    def removeElements(self, head, val):
        g = ListNode
        g.next = head
        n1,n2 = g,head
        while n2:
            if n2.val==val:
                n1.next = n2.next
                n2 = n2.next
            else:
                n1 = n2
                n2 = n2.next
        return g.next