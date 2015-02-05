class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        if head is None or head.next is None:
            return head
        prev = ListNode(0)
        prev.next, p1, p2 = head, head, head
        
        # Split into half
        while p2 is not None:
            prev = p1
            p1 = p1.next
            
            p2 = p2.next
            if p2 is None:
                break
            p2 = p2.next

        list1 = head
        list2 = p1
        prev.next = None
        
        # Reverse list2
        last, p = None, list2
        while p is not None:
            # Swap p and p.next
            nextStep = p.next
            p.next = last
            last = p
            p = nextStep
        list2 = last
        
        # Merge 2 lists
        p1, p2 = list1, list2
        while p1 is not None and p2 is not None:
            nextStep1 = p1.next
            nextStep2 = p2.next
            p1.next = p2
            p2.next = nextStep1
            p1 = nextStep1
            p2 = nextStep2
            
        return