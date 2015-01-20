class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        if len(A) == 1:
            return 0
            
        start , end , last, minStep = 0,0,len(A)-1,0
        
        while start <= end:
            minStep = minStep + 1
            prev = end
            for i in range( start, prev+1):
                
                if i+A[i] >= last:
                    return minStep
                    
                if i+A[i] > end:
                    end = i+A[i]
                    
            print "start: ",start," end: ",end
            start = prev + 1
            
        return 0

s = Solution()
A = [2,3,1,1,4]
print s.jump( A )