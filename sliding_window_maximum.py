class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer[]}
    def maxSlidingWindow(self, nums, k):
        dq = []
        res = []
        for i,n in enumerate(nums):
            while dq!=[] and nums[dq[-1]] <= n:
                dq.pop()
            dq.append(i)
            if dq[0]<=i-k:
                dq.pop(0)
            if i>=k-1:
                res.append( nums[dq[0]] )
        return res