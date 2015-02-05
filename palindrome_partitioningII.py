DEBUG = True
def log(s):
    if DEBUG:
        print s

class Solution:
    def answer(self, s):
        def isPalindrome(s):
            if len(s) <=1:
                return True
            return s==s[::-1] #reversed of s
        N = len(s)
        if N == 0:
            return 0

        # Dynamic Programming
        # dp[i]: min cut from 0-i of s
        # Initialize min-cut as length
        dp = [ i for i in range(N) ]
        
        # Optimization by iterate dp
        for i in range(N):
            if isPalindrome( s[:i+1] ):
                dp[i] = 0
            else:

                # if k to i of s is palindrome, k is palindrome cut
                # Find minimum of all k < i
                for k in range(0,i):
                    if isPalindrome(s[k+1:i+1]):
                        dp[i] = min(dp[i], dp[k]+1)
        return dp[-1]
        

# Testing
s = Solution()
test = "bb"
print "Tesing: ",test
print "Answers: ",s.answer(test) 
                
                 
