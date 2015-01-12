DEBUG = True
def log(s):
    if DEBUG:
        print s

class Solution:
    def rotate(self, matrix):
        n = len(matrix)
        if n < 2:
            return matrix

        # Rotate by layer
        for layer in range(n/2):
            b = layer # begin
            e = n-1-layer # end

            for i in range(e-b):
                swap = matrix[e-i][b]
                matrix[e-i][b] = matrix[e][e-i]
                matrix[e][e-i] = matrix[b+i][e]
                matrix[b+i][e] = matrix[b][b+i]
                matrix[b][b+i] = swap
            print "\nlayer: ",layer
            print "b=",b,"e=",e
            for m in matrix:
                print m
        return matrix

# Testing
s = Solution()
test = [[2,29,20,26,16,28],[12,27,9,25,13,21],[32,33,32,2,28,14],[13,14,32,27,22,26],[33,1,20,7,21,7],[4,24,1,6,32,34]]
print "Tesing: ",test
print "Answers: ", s.rotate( test )
                
                 
