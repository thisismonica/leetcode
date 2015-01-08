class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        if obstacleGrid == []:
            return 0
        iRow = len(obstacleGrid)
        iCol = len(obstacleGrid[0])
        dp =[ [ 0 for i in range(iCol) ] for j in range(iRow) ]
        dp[0][0] = 1 - obstacleGrid[0][0]
        
        for i in range(iRow):
            for j in range(iCol):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                    continue
                if i == 0 and j > 0:
                    dp[i][j] = dp[i][j-1]
                elif j == 0 and i > 0:
                    dp[i][j] = dp[i-1][j]
                elif i > 0 and j > 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[-1][-1]



