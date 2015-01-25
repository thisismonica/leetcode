DEBUG = True
def log(s):
    if DEBUG:
        print s

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def answer(self, lists):
        if lists == []:
            return
        res = ListNode(0)
        curr = res

        # Build heap to store the current order of numbers in each list 
        nums = []
        for l in lists:
            if l is not None: nums.append( (l.val, l) )
        heapq.heapify(nums)

        while nums != []:
            # Pop smallest node from heap top
            (value, node) = heapq.heappop( nums )
            curr.next = node
            curr = node
            
            # Push the next node
            if node.next is not None:
                heapq.heappush( nums, (node.next.val, node) )

        return res.next


        


# Testing
s = Solution()
test = [2,1,2,0,1]
print "Tesing: ",test
print "Answers: ",s.answer(test) 
                
                 
