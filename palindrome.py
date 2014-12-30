class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        if s=="": return []
        if len(s)==1: return [ [s] ]

        self.dp = [ [False for i in range(len(s)) ] for j in range(len(s)) ]
        for i in  range(0,len(s)) :
            for j in reversed( range(i+1) ):
		if i-j <= 1:
		    self.dp[i][j] = (s[i]==s[j])
                else:
                    self.dp[i][j] = ( s[i]==s[j] and self.dp[i-1][j+1] )
        print "dp: ",self.dp
        self.res, self.s = [], s
        self.dfs([],0)
        return self.res
    
    def dfs(self, prevList, start):
        if start==len(self.s):
            self.res.append( prevList )
            return
        
        for i in range( start, len(self.s) ):
            # if substring is palindrome
            if self.dp[i][start]:
                self.dfs(prevList+[ self.s[start:i+1] ], i+1)

s = Solution()
print s.partition("ab")
