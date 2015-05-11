class Solution:
    # @param {string} s
    # @param {string} t
    # @return {integer}
    def numDistinct(self, s, t):
        if len(s) < len(t):
            return 0
        if t == "":
            return 1
        
        dp = [ [0 for j in range(len(t))]  for j in range(len(s)) ]
        dp[0][0] = 1 if s[0]==t[0] else 0
        
        for i in range( 1, len(s) ):
            j = 0
            while j <= i and j < len(t):
                dp[i][j] = dp[i-1][j]
                if s[i] == t[j]:
                    dp[i][j] += dp[i-1][j-1] if j > 0 else 1
                j+=1

    return dp[len(s)-1][len(t)-1]





