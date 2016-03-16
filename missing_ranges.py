class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        def genStr(lower, upper):
            return str(lower) + "->" + str(upper) if upper!=lower else str(lower)
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        if nums == []:
            return [ genStr(lower,upper) ] 
            
        res = []
        if nums[0] > lower:
            res.append( genStr(lower, nums[0]-1) )
            
        i = 0
        while i < len(nums):
            if nums[i] < lower:
                i += 1
                continue
            if nums[i] > upper:
                break
            
            j = i + 1
            while j < len(nums) and nums[j] <= upper and nums[j] == nums[j-1] + 1:
                j += 1
            if j == len(nums) or nums[j] > upper:
                break

            m0, m1 = nums[j-1] + 1, nums[j] - 1
            res.append( genStr(m0, m1) )
            
            i = j
                
        if nums[-1] < upper:
            res.append( genStr(nums[-1]+1, upper) )
            
        return res

s = Solution()
print s.findMissingRanges([0,9],0,9)
            
            