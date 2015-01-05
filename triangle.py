class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        n = len( triangle[-1] )
        dp0 = [0 for i in range(n) ]
        dp1 = [0 for i in range(n) ]
        dp0[0] = triangle[0][0]
        
        for row in triangle[1:]:
            m = len(row)
            dp1[0] = dp0[0] + row[0]
            dp1[m-1] = dp0[m-2] + row[m-1]
            for i in range(1,m-1):
                dp1[i] = min(dp0[i], dp0[i-1]) + row[i]

            # CAREFUL with list copy
            dp0 = dp1[:]

            print "row: ",row, "dp0: ",dp0

        return min(dp0)

# Testing

s = Solution()
test = [ [-1],[2,3],[1,-1,-1]]
print "Tesing: ",test
print "Answers: ",s.minimumTotal(test)
