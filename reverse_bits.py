class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res = 0
        for i in range(32):
            r = n%2
            n >>= 1
            res <<=1
            res += r
        return res