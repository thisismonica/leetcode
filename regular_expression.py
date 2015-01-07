DEBUG = True
def log(s):
    if DEBUG:
        print s

class Solution:
    def answer(self, s, p):
        def matchSingle( c1 , c2 ):
            if c1 == '.' or c2 =='.':
                return True
            else:
                return c1 == c2
        
        s = " "+s
        p = " "+p

        dp = [ [False for j in range(len(p))] for i in range(len(s))]
        
        dp[0][0] = True
        
        # Dynamic Programming
        for i in range(0, len(s)):
            for j in range(1, len(p)):

                if p[j] == '*':
                    star_zero = dp[i][j-2] 
                    star_more = dp[i-1][j] and matchSingle(s[i],p[j-1]) 
                    dp[i][j] = star_zero or star_more

                elif i > 0:
                    dp[i][j]=dp[i-1][j-1] and matchSingle(s[i],p[j])

                log( "dp: "+str(i)+str(j) )
                log( dp[i][j] )

        return dp[-1][-1]


# Testing
s = Solution()
test1 = ""
test2 = "."
print "Tesing: ",test1, test2
print "Answers: ",s.answer(test1, test2) 
                
                 
