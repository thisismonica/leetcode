class Solution:
    # @return an integer
    def minDistance(self, word1, word2):
        dp =  [ [0 for i in range(len(word2)+1) ] for j in range(len(word1)+1) ]
        
        # Initialize dp, get first row and first col
        for i in range(len(word1)+1):
            dp[i][0] = i
        for j in range(len(word2)+1):
            dp[0][j] = j
        
        # Dynamic programming for edit distance
        for i in range(1,len(word1)+1):
            for j in range(1, len(word2)+1):
                dp[i][j] = dp[i-1][j-1] if word1[i-1] == word2[j-1] else min( dp[i][j-1], dp[i-1][j], dp[i-1][j-1])+1

    return dp[len(word1)][len(word2)]
