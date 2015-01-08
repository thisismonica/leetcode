class Solution:
    
    # @return an integer
    def uniquePaths(self, m, n):
        row = [1]*n
        table = [row]*m
        for i in range(1,m):
            for j in range(1,n):
                table[i][j] = table[i-1][j] + table[i][j-1]
        return table[m-1][n-1]
