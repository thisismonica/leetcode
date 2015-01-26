DEBUG = True
def log(s):
    if DEBUG:
        print s

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def __str__(self):
        res = "["
        node = self
        while node is not None:
            res += str(node.val)
            res += "->"
            node = node.next
        res += "None]"
        return res

class List:
    def __init__(self, nums):
        guard = ListNode(0)
        node = guard
        for n in nums:
            new_node = ListNode(n)
            node.next = new_node
            node = new_node
        self.head = guard.next
    def __str__(self):
        res = "["
        node = self.head
        while node is not None:
            res += str(node.val)
            res += "->"
            node = node.next
        res += "None]"
        return res

class Solution:
    def answer(self, head, k):
        guard = ListNode(0)
        guard.next = head
        p1, p2, start = head, head, guard

        while p2 is not None:
            # Move p2 to the end of sublist for reverse
            for i in range(k-1):
                p2 = p2.next
                if p2 is None:
                    return guard.next

            # Reverse between p1, p2
            end = p2.next
            prev_p = end
            p = p1
            while p != end:
               next_p = p.next
               p.next = prev_p
               prev_p = p
               p = next_p
            start.next =  p2
            start = p1
            p1, p2 = end, end

        return guard.next

# Testing
s = Solution()
test = List( [1,2,3,4,5] )
test2 = 4
print "Tesing: ",test, test2
print "Answers: ",s.answer(test.head,test2) 
                
                 
