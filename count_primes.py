class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        import math
        fact = [True]*max(2,n)
        fact[0] = False
        fact[1] = False
        
        for i in range(2, int(math.ceil(math.sqrt(n))) ):
            if fact[i]:
                j = i
                while i*j<n:
                    fact[i*j] = False
                    j+=1
        return sum(fact)