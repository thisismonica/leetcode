class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        if nums == []:
            return 0
        if len(nums) <= 3:
            return max(nums)
        
        money = 0
        money0 = nums[0]
        money1 = max(nums[0], nums[1])
        for i in range( 2, len(nums)-1 ):
            money = max(money1, money0+nums[i])
            money0 = money1
            money1 = money
        max_amount = money
        
        money0 = nums[1]
        money1 = max(nums[1], nums[2])
        for i in range( 3, len(nums) ):
            money = max(money1, money0+nums[i])
            money0 = money1
            money1 = money
        max_amount = max(money, max_amount)
        
        return max_amount
