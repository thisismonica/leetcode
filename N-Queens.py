class Solution:
    # @return a list of lists of string
    def solveNQueens(self, n):
        self.res = []
        self.dfs( n, 0, [-1 for x in range(n)])
        return self.res
        
    def dfs(self, n, iR, board):
        if iR == n:
            answer = [ ["." for i in range(n)] for j in range(n) ]
            for i in range(n):
                answer[i][ board[i] ] = 'Q'
                answer[i] = "".join( answer[i] )
            self.res.append(answer)
            return
              
        for j in range(n):
            valid = True
            for i in range(iR):
                # colume
                if j == board[i]: valid = False; break
                # diagnal
                if abs( board[i] - j) == iR - i: valid = False; break
            if valid:
                board[iR] = j
                self.dfs(n, iR+1, board)
                
        return
                        
    
