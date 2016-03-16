class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # First 5 ugly numbers
        nums = [1,2,3,4,5]
        if n <= len(nums):
            return nums[n-1]
        nums.extend( [-1]*(n-5) )
         
        i2, i3, i5 = 2, 2, 4
        for i in range(5, n):
            nums[i] = min(nums[i2]*2, nums[i3]*3, nums[i5]*5)
            if nums[i] == nums[i2]*2:
                i2 += 1
            if nums[i] == nums[i3]*3:
                i3 += 1
            if nums[i] == nums[i5]*5:
                i5 += 1

        return nums[-1]
        
        
s = Solution()
test = 11
print s.nthUglyNumber(test)