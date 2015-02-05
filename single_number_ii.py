class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        t1,t2,t3 = 0,0,0 # Variable for number occurs 1time, 2 times, 3 times
        
        for num in A:
            # Occur 2 times: same number previously occurred 1 time and then occur again
            t2 = t2 | t1&num
            
            # Occur 1 time: XOR
            t1 ^= num
            
            # Occur 3 times: occur 1 time and occur 2 time
            t3 = ( t2 & t1 )
            
            # Exclude t3 in t1
            t1 = t1 & ~t3
            # Exclue t3 in t2
            t2 = t2 & ~t3
            
        return t1