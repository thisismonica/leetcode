class Solution:
    # @param {string} s1
    # @param {string} s2
    # @param {string} s3
    # @return {boolean}
    def isInterleave(self, s1, s2, s3):
        l1, l2, l3 = len(s1), len(s2), len(s3)
        if l3 != l1+l2:
            return False
        dp = [ [False for i in range(l2+1)] for j in range(l1+1)]
        dp[0][0] = True
        for i in range(1,l1+1):
            dp[i][0] = s1[i-1]==s3[i-1] and dp[i-1][0]
        for j in range(1,l2+1):
            dp[0][j] = s2[j-1]==s3[j-1] and dp[0][j-1]
        
        for i in range(1,l1+1):
            for j in range(1,l2+1):
                if s1[i-1]==s3[i+j-1]:
                    dp[i][j] = dp[i-1][j]
                if s2[j-1]==s3[i+j-1]:
                    dp[i][j] = dp[i][j] or dp[i][j-1]

    return dp[l1][l2]