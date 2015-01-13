DEBUG = True
def log(s):
    if DEBUG:
        print s

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def answer(self, head):

        # First meet
        slow, fast = head, head
        while True:
            if slow is None or fast is None:
                return None
            slow = slow.next
            fast = fast.next
            if fast is None:
                return None
            fast = fast.next
            if slow == fast:
                return None
        
        # Second meet, p1, p2 same speend
        # p1 start from head, p2 start from slow==fast
        p1, p2 = head, slow
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p1

# Testing
s = Solution()
test = [2,1,2,0,1]
print "Tesing: ",test
print "Answers: ",s.answer(test) 
                
                 
