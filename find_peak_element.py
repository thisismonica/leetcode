DEBUG = True
def log(s):
    if DEBUG:
        print s
class Solution:
    # @param num, a list of integer
    # @return an integer
    def findPeakElement(self, num):
        num = [-2147483649] + num + [-2147483649]
        # Binary Search
        left = 1
        right = len(num) - 2
        while left <= right:
            m = (left+right)/2
            # Should not happen if num has at leat 1 peak
            if m == 0 or m == len(num)-1:
                return -1
            
            # Check if m is peak
            if num[m]>num[m-1] and num[m]>num[m+1]:
                return m-1
            
            # if m is descending, left part must has peak
            # if m is ascending, right part must has peak
            if num[m-1] > num[m] and num[m] > num[m+1]:
                right = m-1
            elif num[m-1] < num[m] and num[m] < num[m+1]:
                left = m+1
            else:
                left += 1
        return -1
# Testing
s = Solution()
test = [2,1,2]
print "Tesing: ",test
print "Answers: ",s.answer(test) 
                
                 
