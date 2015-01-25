DEBUG = True
def log(s):
    if DEBUG:
        print s

# Place N Queens on an N*N Board that no 2 Queens attack each other
# Return the number of distinct solutions
class Solution:
    def answer(self, n):
        self.total = 0
        self.dfs( 0, n, [-1 for i in range(n)] )
        return self.total

    def dfs(self,iR, n, board):
        if iR == n:
            self.total += 1
            return
        for j in range(n):
            is_valid = True
            for i in range(iR):
                # Column conflict
                if j == board[i]:
                    is_valid = False
                    break
                # Diagnal conflict
                if abs(board[i]-j) == iR-i:
                    is_valid = False
                    break
            if is_valid:
                board[iR] = j
                self.dfs(iR+1, n, board)
        return



# Testing
s = Solution()
test = 4
expect = 2
print "Tesing: ",test
print "Expecting: ",expect
print "Answers: ",s.answer(test) 
                
                 
