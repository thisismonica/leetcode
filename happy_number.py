class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        occurred = set()
        square = dict([ (c,int(c)**2) for c in "0123456789" ])
        while n!=1 and n not in occurred:
            occurred.add(n)
            n = sum( [square[c] for c in str(n)] )
        return n==1