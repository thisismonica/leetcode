class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        if num==[]: return None
        if len(num)==1: return num[0]
        left, right = 0, len(num)-1
        
        while left < right and num[left] >= num[right]:
            middle = (right+left)/2
            
            # Middle in left subset
            if num[middle] > num[left]:
                left = middle+1
                
            # Middle in right subset
            elif num[middle] < num[right]:
                right = middle
            
            # Middle can be either side
            else:
                left = left+1
                
        return num[left]