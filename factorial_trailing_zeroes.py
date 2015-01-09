DEBUG = True
def log(s):
    if DEBUG:
        print s

class Solution:
    #Given an integer n, return the number of trailing zeroes in n!.
    # Logarithmic time complexity
    def answer(self, n):
        # number of 0 depends on how many '5's before n
        num5 = 0
        while n/5 >0:
            num5 += n/5
            n = n/5
        return num5

# Testing
s = Solution()
test = 1808548329
print "Tesing: ",test
print "Answers: ",s.answer(test) 
                
                 
