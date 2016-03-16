class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        n = len(matrix)
        if n==0:
            return False
        m = len(matrix[0])
        if m==0:
            return False
        if target < matrix[0][0]:
            return False
        
        i, j = 0, m-1
        while i<n and j>=0:
            if matrix[i][j]==target:
                return True
            if matrix[i][j]<target:
                i+=1
            else:
                j-=1
        return False