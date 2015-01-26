DEBUG = True
def log(s):
    if DEBUG:
        print s

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        if head is None:
            return None
            
        p1, p2 = head, head
        for i in range(k):
            p2 = p2.next

            # Go back to head when hit the end, trea linked-list as circle
            if p2 is None:
                p2 = head   
        while p2.next is not None:
            p1, p2 = p1.next, p2.next
        
        p2.next = head
        rotated_head = p1.next
        p1.next = None

        return rotated_head

# Testing
s = Solution()
test = [2,1,2,0,1]
print "Tesing: ",test
print "Answers: ",s.answer(test) 
                
                 
