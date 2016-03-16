DEBUG = True
def log(s):
    if DEBUG:
        print s

class Solution:
    # @param s, a string
    # @return a list of lists of string
    def answer(self, s):
        if s=="": return []
        if len(s)==1: return [ [s] ]
        
        # dp[i][j]: True - if from i to j is palindrome, False - from i to j is not palindrome
        self.dp = [ [False for i in range(len(s)) ] for j in range(len(s)) ]
        for i in  range(0,len(s)) :
            for j in reversed( range(i+1) ):
                if i-j<=1:
                    self.dp[i][j] = s[i]==s[j]
                else:
                    self.dp[i][j] = ( s[i]==s[j] and self.dp[i-1][j+1] )
        
        self.res, self.s = [], s
        
        # Depth first search for enumerate all palindromes
        self.dfs([],0)
        return self.res
    
    def dfs(self, prevList, start):
        # 1 combination of palindrome list
        if start==len(self.s):
            self.res.append( prevList )
            return
        
        for i in range( start, len(self.s) ):
            # if substring is palindrome
            if self.dp[i][start]:
                self.dfs(prevList+[ self.s[start:i+1] ], i+1)

# Testing
s = Solution()
test = "sseeslaveidemonstrateyetartsnomedievalseeseeslaveidemonstrateyetartsnomedievalsees"
print "Tesing: ",test
print "Answers: ",s.answer(test) 
                
                 
