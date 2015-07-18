class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def productExceptSelf(self, nums):
        n = len(nums)
        res = [1]*n
        
        product = 1
        for i in reversed(range(n-1)):
            product = product * nums[i+1]
            res[i] = product
        
        product = 1
        for i in range(n):
            res[i] = res[i] * product
            product = product * nums[i]

        return res