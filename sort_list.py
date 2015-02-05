# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, head):
        def split(head):
            if head is None or head.next is None:
                return head, None
            p1 = head
            p2 = head
            while p2 is not None and p2.next is not None:
                p2 = p2.next.next
                if p2 is None:
                    break
                p1 = p1.next
            
            l2 = p1.next
            p1.next = None
            return head, l2
        
        def merge(p1, p2):
            res = ListNode(0)
            cur = res
            while True:
                if p1 is None:
                    cur.next = p2
                    break
                if p2 is None:
                    cur.next = p1
                    break
                
                if p1.val < p2.val:
                    cur.next = p1
                    p1 = p1.next
                else:
                    cur.next = p2
                    p2 = p2.next
                cur = cur.next
                
            return res.next
                
        def mergesort(head):
            if head is None or head.next is None:
                return head
                
            p1,p2 = split(head)
            p1 = mergesort(p1)
            p2 = mergesort(p2)
            head = merge(p1, p2)
            return head
            
        return mergesort(head)