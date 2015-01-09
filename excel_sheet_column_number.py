DEBUG = True
def log(s):
    if DEBUG:
        print s

class Solution:
    def answer(self, s):
        col = 0
        for c in s:
            col = col*26 + ord(c) - ord('A') + 1
        return col

# Testing
s = Solution()
test = "AA"
print "Tesing: ",test
print "Answers: ",s.answer(test) 
                
                 
