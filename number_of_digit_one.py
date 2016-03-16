class Solution:
    # @param {integer} n
    # @return {integer}
    def countDigitOne(self, n):
        if n <= 0:
            return 0
        size = 1
        res = 0
        low = 0
        high = n
        while high > 0:
            curr = high%10
            high = high/10
            if curr == 0:
                res += high*size
            elif curr == 1:
                res += high*size + (low+1)
            else:
                res += high *size + size
            low = curr*size + low
            size *= 10
        return res