class Solution:
    def largestRectangleArea(self, height):
        stack = []
        i = 0
        maxArea = 0
        while i < len(height):
            if stack==[] or height[ stack[-1] ] <= height[i]:
                stack.append( i )
                i = i+1
            else:
                num = stack.pop()
                if stack!=[]:
                    area = height[num] * (i - stack[-1] -1)
                else:
                    area = height[num] * (i)
                maxArea = max(maxArea, area)
    
        while stack != []:
            num = stack.pop()
            if stack!=[]:
                area = height[num]*(i-stack[-1]-1)
            else:
                area = height[num]*i
            maxArea = max(maxArea, area)

                return maxArea
                    
                    # @param matrix, a list of lists of 1 length string
                    # @return an integer
                    def maximalRectangle(self, matrix):
numRow = len(matrix)
    if numRow== 0:
        return 0
        numCol = len(matrix[0])
        height = [ [ 0 for i in range(numCol)] for j in range(numRow) ]
        height[0] = [ int(num) for num in matrix[0] ]
        
        for i in range(1,numRow):
            matrix[i] = list( matrix[i] )
            for j in range(numCol):
                if matrix[i][j] == "1":
                    height[i][j] = height[i-1][j] + 1
    maxArea = 0
        for i in range(numRow):
            area = self.largestRectangleArea(height[i])
            maxArea = max(area, maxArea)
return maxArea
