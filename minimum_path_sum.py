class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        # Create matrix to store min value
        nRow = len(grid)
        nCol = len(grid[0])
        dp = [[ 0 for i in range(nCol) ] for j in range(nRow) ]
        
        # Initialize matrix
        dp[0][0] = grid[0][0]
        for i in range(1,nCol):
            dp[0][i] = dp[0][i-1] + grid[0][i]
        for j in range(1,nRow):
            dp[j][0] = dp[j-1][0] + grid[j][0]
        
        # Dynamic programming for min path
        for i in range(1,nRow):
            for j in range(1,nCol):
                dp[i][j] = grid[i][j] + min( dp[i][j-1], dp[i-1][j] )

    return int(dp[nRow-1][nCol-1])