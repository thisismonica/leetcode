DEBUG = True
def log(s):
    if DEBUG:
        print s

class Solution:
    def answer(self, n, k):
        def fac(n):
            res = 1
            while n > 1:
                res *= n
                n -= 1
            return res

        res = ""
        num = range(1, n+1)
        for i in range(1, n+1 ):
            # Choose ith elem in result
            # k-1 to make zero-based number
            id_i = (k-1)/fac(n-i)
            res += str( num[id_i] )

            # Update k and num for next elem
            del num[id_i]
            k = k - fac(n-i)*(id_i)
        return res
            
            


# Testing
s = Solution()
test1 = 3
test2 = 3
expect = "213"
print "Expecting: ", expect
print "Tesing: ",test1, test2
print "Answers: ",s.answer(test1, test2) 
                
                 
