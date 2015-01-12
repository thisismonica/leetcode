DEBUG = True
def log(s):
    if DEBUG:
        print s

class Solution:
    def search(self, A, target):
        if A == []:
            return False
        if len(A) == 1:
            return A[0] == target
                                        
        mid = len(A)/2
        return self.search(A[:mid],target) or self.search(A[mid:],target)


# Testing
s = Solution()
A = []
target = 
print "Tesing: ",A, target
print "Answers: ",s.answer(A, target) 
                
                 
