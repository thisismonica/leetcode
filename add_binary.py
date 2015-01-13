DEBUG = True
def log(s):
    if DEBUG:
        print s

class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        a, b = list(a), list(b)
        a.reverse()
        b.reverse()
        
        # Add zero for shorter length number
        diff = len(a) - len(b)
        if diff > 0:
            b.extend( ['0' for i in range(diff)] )
        else:
            a.extend( ['0' for i in range(-diff)] )
        
        # Adding    
        res = ""
        c = False
        for i in range( len(a) ):
            ai = a[i] == '1'
            bi = b[i] == '1'
            ri = c^ai^bi #sum
            c = (ai and bi) or ( (ai or bi) and c) #carry
            if ri:
                res += '1'
            else:
                res += '0'
        if c:
            res += '1'
        return res[::-1]
            
# Testing
s = Solution()
test1 = "1"
test2 = "111"
print "Tesing: ",test1,test2
print "Answers: ",s.addBinary(test1, test2) 
                
                 
