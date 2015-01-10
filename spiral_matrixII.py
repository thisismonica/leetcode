DEBUG = True
def log(s):
    if DEBUG:
        print s

class Solution:
    '''
    Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.
    [1,2,3]
    [8,9,4]
    [7,6,5]
    '''

    def generateMatrix(self, n):
        if n < 1:
            return []
        if n == 1:
            return [[1]]
        m =[ [0 for i in range(n)] for j in range(n) ]

        # Generate edge first
        # 1) up edge
        edge = 0
        for i in range(n):
            edge += 1
            m[0][i] = edge
        # 2) right edge
        for j in range(1,n):
            edge += 1
            m[j][n-1] = edge
        # 3) bottome edge
        for q in reversed( range(n-1) ):
            edge += 1
            m[n-1][q] = edge
        # 4) left edge
        for p in reversed( range(1,n-1) ):
            edge += 1
            m[p][0] = edge

        # Fill inside of matrix recursively
        inside = self.generateMatrix(n-2)
        for i in range(1,n-1):
            for j in range(1,n-1):
                m[i][j] = inside[i-1][j-1] + edge
        return m
            
# Testing
s = Solution()
test = 4
print "Tesing: ",test
print "Answers: ",s.generateMatrix(test) 
