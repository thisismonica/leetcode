class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @param {integer} t
    # @return {boolean}
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if len(nums) < 2:
            return False
        
        index = {}
        for i in range( len(nums) ):
            if nums[i] in index:
                index[nums[i]].append(i)
            else:
                index[nums[i]] = [i]
        
        nums.sort()
        i = 0
        while i < len(nums):
            # find i'th nearest almost duplicate
            j = i+1
            while j < len(nums) and nums[j] - nums[i] <= t:
                if self.checkIndexDistance(index[nums[i]], index[nums[j]], k):
                    return True
                j += 1
            i += 1
        return False
    
    def checkIndexDistance(self,i0,i1,dis):
        for i in i0:
            for j in i1:
                if i!=j and abs(i-j) <= dis:
                    return True
        return False