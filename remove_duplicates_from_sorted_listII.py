# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        guard = ListNode(0)
        guard.next = head
        p, q = guard, head
        hasDup = False
        
        while q:
            while q.next and q.next.val == q.val:
                hasDup = True
                q = q.next
            
            # Delete
            if hasDup:
                q = q.next
                p.next = q
                hasDup = False
            else:
                p = p.next
                q = q.next
        return guard.next