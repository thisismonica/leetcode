class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        # Initialize 2 guard nodes, 2 pointers
        g1 = ListNode(0)
        g2 = ListNode(0)
        p1, p2 = g1, g2
        
        p = head
        while p is not None:
            # Append to list 1
            if p.val < x:
                p1.next = p
                p1 = p
            # Append to list 2
            else:
                p2.next = p
                p2 = p
            p = p.next
            
        # Connect 2 lists
        p1.next = g2.next
        
        # Clear the last element
        p2.next = None
        
        return g1.next