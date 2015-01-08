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

        # Dynamic Programming
        # dp[i] == s[:i+1] is word break
        for i in range(N):
            # if itself is a word, then its True
            if s[:i+1] in dict:
                dp[i] = True
            else:
                # find k that previous k is word break, (k-i) is a word
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
                
                 
