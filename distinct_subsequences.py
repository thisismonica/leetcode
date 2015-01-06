class Solution:
    def numDistinct(self, S, T):
        dp = [ [ 0 for i in range(len(S))] for j in range( len(T) )]
        
        print "\ndp: ",dp

        # Calculate dp[0][i] when susbsequence T has 1 elem
        dp[0][0] = 1 if S[0]==T[0] else 0
        for i in range(1, len(S) ):
            if S[i] == T[0]:
                dp[0][i] = dp[0][i-1] + 1
            else:
                dp[0][i] = dp[0][i-1]

        print "\ndp: ",dp
        for i in range( 1, len(S) ):
            for j in range( 1, len(T) ):
                if j <= i:
                    if S[i] == T[j]:
                        dp[j][i] = dp[j-1][i-1] + dp[j][i-1]
                    else:
                        dp[j][i] = dp[j][i-1]
        print "\ndp: ",dp

        return dp[-1][-1]

# Testing
s = Solution()
test1 = "B"
test2 = "B"
print "Testing: ",test1," ",test2
print "Answer: ",s.numDistinct(test1,test2)

