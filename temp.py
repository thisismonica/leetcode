class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        N = len(s)
        self.palin = [ [False for i in range(N)] for j in range(N)]
        for i in range(N):
            self.palin[i][i] = True
        
        for i in reversed(range(N-1)):
            self.palin[i][i+1] = s[i]==s[i+1]
            for j in range(i+2,N):
                if self.palin[i+1][j-1] and s[i]==s[j]:
                    self.palin[i][j] = True
        
        self.s = s
        self.result = []
        self.getPart([],0)
        return self.result
    
    def getPart(self, part, start):
        if start==len(self.s):
            self.result.append( part )
            return
        for i in range(start, len(self.s)):
            if self.palin[start][i]:
                self.getPart( part + [ self.s[start:i+1] ], i+1 )

s = Solution()

test = "seeslaveidemonstrateyetartsnomedievalsees"
print "Test: ",test
print "Result: ",s.partition(test)
