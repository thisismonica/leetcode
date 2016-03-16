class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        if target< matrix[0][0]:
            return False

        nRow = len(matrix)
        nCol = len(matrix[0])
        targetRow = -1
        
        begin, end = 0, nRow-1
        while begin <= end:
            mid = (begin+end)/2
            if matrix[mid][0] <= target and matrix[mid][nCol-1] >= target:
                targetRow = mid
                break
            elif matrix[mid][-1] < target:
                begin = mid + 1
            else:
                end = mid - 1
        if targetRow == -1:
            return False
        
        begin, end = 0, nCol-1
        while begin <= end:
            mid = (begin+end)/2
            if matrix[targetRow][mid] == target:
                return True
            elif matrix[targetRow][mid] < target:
                begin = mid + 1
            else:
                end = mid - 1
        return False
        
s = Solution()
matrix = [[1,3]]
target = 3
print "Result: ",s.searchMatrix(matrix, target)
        
        
            