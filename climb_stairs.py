class Solution:
    # @param {integer} n
    # @return {integer}
    def climbStairs(self, n):
        if n < 3 :
            return n
        
        ways_prev_prev = 1
        ways_prev = 2
        for i in range(3, n+1):
            ways = ways_prev + ways_prev_prev
            ways_prev_prev = ways_prev
            ways_prev = ways
        return ways

