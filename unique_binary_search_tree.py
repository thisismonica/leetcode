class Solution:
    # @param {integer} n
    # @return {integer}
    def numTrees(self, n):
        dp = [1] * (n+1)
        dp[0] = 1
        for i in range(1,n+1):
            dp[i] = 0
            for j in range(i):
                dp[i] += dp[j]*dp[i-1-j]

    return dp[n]