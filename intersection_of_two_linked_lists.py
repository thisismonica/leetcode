DEBUG = True
def log(s):
    if DEBUG:
        print s

class ListNode:
    def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
    def answer(self, headA, headB):
        # Length of 2 linked-lists
        p = headA
        lenA = 0
        while p is not None:
            p = p.next
            lenA += 1
        p = headB
        lenB = 0
        while p is not None:
            p = p.next
            lenB += 1

        # Determine long list and short list
        if lenA > lenB:
            long_list_node, short_list_node = headA, headB
            diff = lenA - lenB
        else:
            long_list_node, short_list_node = headB, headA
            diff = lenB - lenA

        # Start long_list_node first
        for i in range(diff):
            long_list_node = long_list_node.next

        # Iterate 2 lists to find intersection
        while long_list_node is not None and short_list_node is not None:
            if long_list_node is short_list_node:
                return long_list_node
            long_list_node = long_list_node.next
            short_list_node = short_list_node.next

        return None


# Testing
s = Solution()

print "Tesing: ",test
print "Answers: ",s.answer(test) 
                
                 
