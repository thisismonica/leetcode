DEBUG = True
def log(s):
    if DEBUG:
        print s

class Solution:
    def answer(self, s, dict):
        N = len(s)
        if N==0:
            return True
        dp = [False for i in range(N)]

        for i in range(N):
            if s[:i+1] in dict:
                dp[i] = True
            else:
                for k in range(0,i):
                    if dp[k] and s[k+1:i+1]in dict:
                        dp[i] = True
                        break
        return dp[-1]

# Testing
s = Solution()
test1 = "leetcode"
test2 = ["leet","code"]
print "Tesing: ",test1, test2
print "Answers: ",s.answer(test1, test2) 
                
                 
