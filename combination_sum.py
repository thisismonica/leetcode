DEBUG = True
def log(s):
    if DEBUG:
        print s

class Solution:
    '''
    Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.
    - All numbers positive
    - Elements in solution set should be non-descending
    - same repeated number from C is OK
    C=[2,3,6,7], target = 7
    Answer = [2,2,3]
    '''
    
    def answer(self, candidate, target):


# Testing
s = Solution()
test = [2,3,6,7]
print "Tesing: ",test
print "Answers: ",s.answer(test) 
                
                 
