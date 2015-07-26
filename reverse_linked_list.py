# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        n1,n2 = None, head
        while n2:
            n3 = n2.next
            n2.next = n1
            n1, n2 = n2,n3
        return n1