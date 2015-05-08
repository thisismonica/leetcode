class Solution:
    # @param {string} s
    # @return {integer}
    def numDecodings(self, s):
        if len(s)==0:
            return 0
        ways, prev_ways, prev_prev_ways = 0,0,1
        if s[0] != '0':
            prev_ways = 1
        if len(s) == 1:
            return prev_ways
        
        for i in range( 1,len(s) ):
            ways = 0
            if s[i] != '0':
                ways += prev_ways
            if int(s[i-1:i+1]) <= 26 and int(s[i-1:i+1]) >= 10:
                ways += prev_prev_ways
            prev_prev_ways = prev_ways
            prev_ways = ways
        return ways

# Testing

s = Solution()
line = '101'
print "Tesing: ",line
print "Answers: ",s.numDecodings(line)
