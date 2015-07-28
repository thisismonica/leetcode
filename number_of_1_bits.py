class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        h = 0
        while n>0:
            h += n%2
            n >>= 1
        return h