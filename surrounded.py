class Solution:
    # @param board, a 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def neighbors(self,pos,N,M):
        y, x = pos[0], pos[1]
        neighbors = []
        if x-1 >=0:
            neighbors.append( (y, x-1) )
        if x+1 <M:
            neighbors.append( (y, x+1) )
        if y-1 >=0:
            neighbors.append( (y-1, x) )
        if y+1 <N:
            neighbors.append( (y+1, x) )
        return neighbors
        
    def solve(self, board):
        if board == []: return
        edge_circles = []
        not_surr_circles = set()
        N = len(board)
        M = len(board[0])
        # Check matrix edges for circles
        for i in range(N):
            for j in [0, M-1]:
                if board[i][j] != 'X':
                    edge_circles.append( (i,j) )
                    #not_surr_circles[ (i,j) ] = True
        for j in range(1,M-1):
            for i in [0, N-1]:
                if board[i][j] != 'X':
                    edge_circles.append( (i,j) )
                       #not_surr_circles[ (i,j) ] = True
        # DFS each edge circles for and not surrounded circles
        for c in edge_circles:
            stack = [c]
            while stack!=[]:
                print "stack: ",stack
                curr = stack.pop()
                not_surr_circles.add( curr )
                for n in self.neighbors(curr, N, M):
                    if board[n[0]][n[1]] != 'X' and n not in not_surr_circles:
                        stack.append(n)
                        not_surr_circles.add(n)
                        
        print not_surr_circles
        # Flip circles that are surrounded
        for i in range(1,N-1):
            for j in range(1,M-1):
                if board[i][j] != 'X' and (i,j) not in not_surr_circles:
                    board[i][j] = 'X'
        return       
       
s = Solution()
board = ['OXO','XOX','OXO']
for i in range( len(board) ):
    board[i] = list( board[i] )
s.solve( board )
print board
