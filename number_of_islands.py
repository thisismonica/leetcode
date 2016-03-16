class Solution:
    # @param {character[][]} grid
    # @return {integer}
    def numIslands(self, grid):
        if grid == []:
            return 0
        n, m = len(grid), len(grid[0])
        lands = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    lands += 1
                    queue = [ (i,j) ]
                    grid[i][j] = '0'
                    while queue != []:
                        p, q = queue.pop(0)
                        if q+1!=m and grid[p][q+1]=='1':
                            queue.append( (p,q+1) )
                            grid[p][q+1] = '0'
                        if q-1!=-1 and grid[p][q-1]=='1':
                            queue.append( (p,q-1) )
                            grid[p][q-1] = '0'
                        if p-1!=-1 and grid[p-1][q]=='1':
                            queue.append( (p-1,q) )
                            grid[p-1][q] = '0'
                        if p+1!=n and grid[p+1][q]=='1':
                            queue.append( (p+1,q) )
                            grid[p+1][q] = '0'
        return lands
#test = ['11000','11000','00100','00011']
test = ["11111011111111101011","01111111111110111110","10111001101111111111","11110111111111111111","10011111111111111111","10111111011101110111","01111111111101101111","11111111111101111011","11111111110111111111","11111111111111111111","01111111011111111111","11111111111111111111","11111111111111111111","11111011111110111111","10111110111011110111","11111111111101111110","11111111111110111100","11111111111111111111","11111111111111111111","11111111111111111111"]
test =[ list(s) for s in test]
s = Solution()
print s.numIslands(test)
