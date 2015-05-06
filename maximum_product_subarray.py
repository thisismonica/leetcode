class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, nums):
        minp = [0] * len(nums)
        maxp = [0] * len(nums)
        minp[0], maxp[0] = nums[0], nums[0]

        for i in range(1, len(nums) ):
            minp[i] = min( minp[i-1]*nums[i], maxp[i-1]*nums[i], nums[i])
            maxp[i] = max( minp[i-1]*nums[i], maxp[i-1]*nums[i], nums[i])
        return max( maxp )

