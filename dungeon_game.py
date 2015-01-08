DEBUG = True
def log(s):
    if DEBUG:
        print s

class Solution:
    def answer(self, dungeon):
        if dungeon == []:
            return 0

        N = len(dungeon) # num of rows
        M = len(dungeon[0]) # num of cols

        # Dynamic Programming
        # state dp[i][j]: min HP needed at dunegon(i)(j)
        dp = [ [ 1 for j in range(M)] for i in range(N)]

        # Initial certain value: Last gird with princess
        # Need min HP of (1-dungeon[-1][-1]) if dungeon[-1][-1] is negative
        dp[N-1][M-1] = max(1, -dungeon[N-1][M-1]+1 )
        for i in reversed( range(N-1) ):
            dp[i][M-1] = max(dp[i+1][M-1],1)-dungeon[i][M-1]
        for j in reversed( range(M-1) ):
            dp[N-1][j] = max(dp[N-1][j+1],1) -dungeon[N-1][j]

        # Dependency: current dp depends on next step dp
        for i in reversed( range(N-1) ):
            for j in reversed( range(M-1) ):
                # HP needed for next optimal step
                HP_next_step = max(1, min(dp[i+1][j],dp[i][j+1]) )
                
                # if current dungeon is positive,HP for next decrease
                # HP at least should be 1
                dp[i][j] =  max(1,HP_next_step-dungeon[i][j])
        return dp[0][0]

# Testing
s = Solution()
test = [[2,1],[1,-1]]
print "Tesing: ",test
print "Answers: ",s.answer(test) 
                
                 
