class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        candidates.sort()
        self.res = []
        self.dfs(candidates, 0, target, [])
        return self.res

    def dfs(self, nums, start, target, comb):
        if target == 0:
            self.res.append(comb)
            return

        if target < nums[start]:
            return

        for i in range(start, len(nums)):
            self.dfs(nums, i, target - nums[i], comb + [nums[i]])