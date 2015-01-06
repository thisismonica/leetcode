class Solution:
    # @return a boolean
    def isScramble(self, s1, s2):
        n = len(s1)
        if n!=len(s2):
            return False
        if n == 0:
            return True
        if n == 1:
            return s1[0] == s2[0]
        if s1 == s2:
            return True

        # Initialize 3D Dynamic Programming
        dp = [ [ [ False for k in range(n+1) ] for j in range(n)] for i in range(n)]

        # Calculate starting value of DP
        for i in range( n ):
            for j in range( n ):
                if s1[i] == s2[j]:
                    dp[i][j][1] = True

        # Iterate for DP
        for i in reversed( range(n) ):
            for j in reversed( range(n) ):
                maxLen = min(n-i, n-j)
                for Len in range(1, maxLen+1):

                    # Solve subproblem by trying all possible splits of string
                    # Any split that shows scramble means the 2 strings are scrambled
                    for k in range(1, Len):

                        # left of s1 match left of s2, and right s1 match right s2 (match means is scrambled)
                        left_left_match = dp[i][j][k] and dp[i+k][j+k][Len-k]
                        # left of s1 match right of s2, and right s1 match left s2 (match means is scrambled)
                        left_right_match = dp[i][j+Len-k][k] and dp[i+k][j][Len-k]

                        if left_left_match or left_right_match:
                            dp[i][j][Len] = True
                            break
        return dp[0][0][n]


# Testing
s = Solution()
test1 = "great"
test2 = "rgtae"
print "Testing: ",test1,test2
print "Answer: ",s.isScramble(test1, test2)
