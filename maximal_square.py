class Solution:
    # @param {character[][]} matrix
    # @return {integer}

    def maximalSquare(self,matrix):
        if matrix == []:
            return 0
        

    # Too much timing complexity
    def maximalSquare1(self, matrix):
        if matrix == []:
            return 0
        
        max_square = 0
        nRow = len(matrix)
        nCol = len(matrix[0])
        
        for i in range(nRow):
            for j in range(nCol):
                if matrix[i][j] == '1':
                    n = 1
                    while i+n < nRow and j+n < nCol:
                        row = matrix[i+n][j:j+n+1]
                        col =  ''.join( [ matrix[i+k][j+n] for k in range(n+1) ])
                        if row!= '1'*(n+1) or col!='1'*(n+1):
                            break
                        n += 1
                    max_square = max( max_square, n*n )
        return max_square

    # Too complicated
    def maximalSquare2(self, matrix):
        if matrix == []:
            return 0
        
        max_square = 0
        nRow = len(matrix)
        nCol = len(matrix[0])
        
        height = [[0 for i in range(nCol)] for j in range(nRow)]
        height[0] =[ 1 if c=='1' else 0 for c in matrix[0] ]
        for i in range(1,nRow):
            for j in range(nCol):
                if matrix[i][j] == '1':
                    height[i][j] = height[i-1][j] + 1
                else:
                    height[i][j] = 0
        stack = []
        for i in range(nRow):
            max_square = max( max_square, self.maximalSquareHist(height[i]) )
        return max_square
    
    def maximalSquareHist(self,h):
        if h == []:
            return 0
        h = [0] + h + [0]
        stack = []
        i = 0
        max_square = 0
        while i < len(h):
            if stack == []:
                stack.append(i)
                i += 1
            elif h[i] >= h[ stack[-1] ]:
                stack.append(i)
                i += 1
            else:
                j = stack.pop()
                width = i-stack[-1]-1
                if width >= h[j]:
                    max_square = max(max_square, h[j]*h[j])
    
        # clear stack
        while len(stack) >= 2:
            j = stack.pop()
            width = i-stack[-1] - 1
            if width >= h[j]:
                max_square = max( max_square, h[j]*h[j] )
        return max_square



s = Solution()
test = ["111","111","111"]
print s.maximalSquare(test)
