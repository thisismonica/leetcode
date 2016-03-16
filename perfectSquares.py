class Solution(object):
    ss = [0]
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        for i in range(1, n+1):
            self.ss.append(i)
            j = 1
            while j*j <= n:
                self.ss[i] = min(self.ss[i], 1 + self.ss[i-j*j])
                j += 1

        return self.ss[-1]
                    
test = 7217
s = Solution()
print "result for: ",test, " is: "
print s.numSquares(test)