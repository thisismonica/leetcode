class Solution:
    def generate(self, numRows):
        res = []
        if numRows < 1:
            return res
        prevRow = [1]
        res.append( prevRow )
        
        for i in range(2, numRows+1):
            row = [0 for j in range(i)]
            row[0] = prevRow[0 ]#First
            row[i-1]= prevRow[i-2] #Last

            for k in range(1, i-1):
                row[k] = prevRow[k] + prevRow[k-1]

            res.append( row )
            prevRow = row[:]
        return res
# Testing

s = Solution()
test = 5
print "Tesing: ",test
print "Answers: ",s.generate(test) 
        
       
