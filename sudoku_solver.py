DEBUG = True
def log(s):
    if DEBUG:
        print s

class Solution:
    def isValid(self, num, board, i, j):
        # num in row
        if num in board[i]:
            return False
        # num in col
        if num in [board[k][j] for k in range( len(board) )]:
            return False
        # num in block
        block_row = i / 3
        block_col = j / 3
        for ri in range(3):
            for ci in range(3):
                if num in board[block_row*3+ri][block_col*3+ci]:
                    return False
        return True

    # DFS: recursive solution
    # index : 0(0,0) - 80(8,8)
    def solve(self, board, index):
        if index > 80:
            return True
        i, j = index/9, index%9

        # Find possible number for empty grid
        if board[i][j] == '.':
            num = [str(k) for k in range(1,10) ]
            for n in num:
                if self.isValid( n, board, i, j):
                    board[i][j] = n
                    if self.solve(board, index+1):
                        return True
                    else:
                        board[i][j] = '.'
            return False
        else:
            return self.solve(board, index+1)
            
    def answer(self, board):
        res = self.solve(board, 0)    
        print board
        return res

# Testing
s = Solution()
test =[ [5,3,0,0,7,0,0,0,0 ],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]]

for i in range(len(test)):
    for j in range(len(test[0])):
        if test[i][j] == 0:
            test[i][j] = '.'
        else:
            test[i][j] = str( test[i][j] )
print "Tesing: ",test
print "Answers: ",s.answer(test) 
                
                 
