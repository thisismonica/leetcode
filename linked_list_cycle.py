class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        if head is None or head.next is None:
            return False
            
        p1, p2 = head, head.next.next
        while p2 and p1!=p2:
            p1 = p1.next
            p2 = p2.next
            if p2 is None:
                break
            p2 = p2.next
        if p2:
            return True
        else:
            return False