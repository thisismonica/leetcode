DEBUG = True
def log(s):
    if DEBUG:
        print s

class Solution:
    '''
    Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.
    00 - 0
    01 - 1
    11 - 3
    10 - 2
    '''

    def grayCode(self, n):
        if n == 0:
            return [0]
        if n == 1:
            return [0,1] 

        # First half start from 0, same as gray code (n-1)
        prev = self.grayCode( n-1 )            
        res = prev
        
        # Second half start from 1, plus gray code(n-1) in reverse order
        res += [ g+ (1<<(n-1)) for g in reversed( prev )] 
        return res



# Testing
s = Solution()
test = 3
print "Tesing: ",test
print "Answers: ",s.grayCode(test) 
                
                 
