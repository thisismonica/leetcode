class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        if num==[]: return None
        if len(num)==1: return num[0]
        
        # Binary search for minimum
        left, right = 0, len(num)-1
        while left<right and num[left]>num[right]:
            mid = (left+right)/2
            
            # left subarray ascending, min in right
            if num[mid] >= num[left]:
                left = mid+1
            # right subarray ascending, min in left
            elif num[mid] <= num[right]:
                right = mid
    
        return num[left]