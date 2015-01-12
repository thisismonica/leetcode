DEBUG = True
def log(s):
    if DEBUG:
        print s

class Solution:
    '''
    Given an integer of m*n, return all elements in spiral order
    [1,2,3]
    [8,9,4]
    [7,6,5]
    '''

    def spiralOrder(self, matrix):
        print ("matrix: ")
        for m in matrix:
            print m

        if matrix == []:
            return []
        res = []
        R = len(matrix)
        C = len(matrix[0])
        if C == 0:
            return []

        # Start with 4 edges
        # up edge
        for i in range(C):
            res.append( matrix[0][i] )

        # right edge
        for j in range(1, R):
            res.append( matrix[j][-1] )
        
        # bottom
        if R-1 != 0:
            for i in reversed( range(C-1) ):
                res.append( matrix[-1][i] )

        # left
        if C-1 != 0:
            for j in reversed( range(1, R-1)):
                res.append( matrix[j][0] )

        # Add inner matrix recursively
        m = [ [0 for i in range(1,C-1)] for j in range(1,R-1) ]
        for i in range(1, R-1):
            for j in range(1, C-1):
                m[i-1][j-1] = matrix[i][j]
        return res + self.spiralOrder(m)

# Testing
s = Solution()
test = [[1],[2],[3],[4]]
print "Tesing: ",test
print "Answers: ",s.spiralOrder(test) 
