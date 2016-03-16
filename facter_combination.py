class Solution(object):
    """
    :type n: int
    :rtype: List[List[int]]
    """
    def getFactors(self, n):
        return self.getFactorsComb(n, self.getFacValuesStartFrom(n, 2))

    def getFactorsComb(self, n, factors):
        combs = []
        for f in factors:
            if n/f < f:
                break
            combs.append([f, n/f])
            for c in self.getFactorsComb(n/f, self.getFacValuesStartFrom(n/f, f)):
                combs.append([f] + c)
        return combs

    def getFacValuesStartFrom(self, num, start):
        facs1 = []
        facs2 = []
        upper = num
        i = start
        while i < upper:
            if num%i == 0:
                facs1.append(i)
                upper = num/i
                if upper != i:
                    facs2.append(upper)
            i += 1
        facs2.reverse()
        return facs1 + facs2

s = Solution()
test = 24
print s.getFactors(test)