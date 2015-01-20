DEBUG = True
def log(s):
    if DEBUG:
        print s

class Solution:
    def answer(self, A):
        if A == []:
            return True
        # 1D DP
        # Record redundant steps from last
        redundant = [-1 for i in range(len(A))]
        redundant[0] = 0 # For the first step, no redundant

        for i in range(1,len(A)):
            redundant[i] = max(A[i-1],redundant[i-1]) -1 
            if redundant[i] < 0:
                return False
        return redundant[-1]>=0

# Testing
s = Solution()
test = [3,2,1,0,4]
expect = False
print "Tesing: ",test
print "Expecting: ",expect
print "Answers: ",s.answer(test) 
                
                 
