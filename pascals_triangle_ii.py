class Solution:
    # @param {integer} rowIndex
    # @return {integer[]}
    def getRow(self, rowIndex):
        res = [0]*(rowIndex+1)
        res[-1] = 1
        for i in range(1,rowIndex+1):
            for j in range(rowIndex-i,rowIndex):
                res[j] += res[j+1]
        return res