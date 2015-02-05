class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        if head is None or head.next is None :
            return head
            
        outer, helper =head,  ListNode(0)
        helper.next = head
        
        while outer.next:
            next_node = outer.next
            if outer.next.val < outer.val:
                inner = helper
                # Go to position
                while inner.next.val < outer.next.val:
                    inner = inner.next
                # Insert outer.next between inner and inner.next
                tmp = next_node.next
                next_node.next = inner.next
                inner.next = next_node
                outer.next = tmp
            else:
                outer = next_node
            
        return helper.next