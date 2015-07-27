class Solution:
    # @param {integer} n
    # @return {boolean}
    def isPowerOfTwo(self, n):
        two = 1
        while n>=two:
            if n==two:
                return True
            two <<= 1
        return False