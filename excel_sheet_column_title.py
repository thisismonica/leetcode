DEBUG = True
def log(s):
    if DEBUG:
        print s

class Solution:
    def answer(self, num):
        diff = ord('A') - 1
        res = ""
        while num > 0:
            n = num % 26
            #  1 - 25 : 'A' - 'Y'
            #  0: 'Z'
            # Special case at residual==0
            if n == 0:
                n = 26
                num = num/26 - 1
            else:
                num = num/26
            res = str( unichr(n+diff) ) + res
        return res

# Testing
s = Solution()
test = 26
print "Tesing: ",test
print "Answers: ",s.answer(test) 
                
                 
