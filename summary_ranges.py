class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        ranges = []
        i = 0
        while i < len(nums):
            j = i+1
            while j<len(nums) and nums[j]==nums[j-1]+1:
                j+=1
            if j-1==i:
                ranges.append( str(nums[i]) )
            else:
                ranges.append( str(nums[i])+'->'+str(nums[j-1]))
            i = j
        return ranges