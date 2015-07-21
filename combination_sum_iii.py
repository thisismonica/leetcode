class Solution:
    # @param {integer} k
    # @param {integer} n
    # @return {integer[][]}
    def combinationSum3(self, k, n):
        return self.dfs( [1,2,3,4,5,6,7,8,9], n, k)
    
    def dfs(self, nums, target, size):
        if size < 1 or target < 1:
            return []
        if size == 1:
            return [ [target] ] if target in nums else []
        
        res = []
        for i in range(len(nums)):
            for c in self.dfs( nums[i+1:], target-nums[i], size-1 ):
                res.append( [nums[i]]+c )
        return res
