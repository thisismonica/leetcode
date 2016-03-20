__author__ = 'monica_wang'
import math

class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        r = 0
        count = 0
        i = 0
        while r < n:
            if i >= len(nums) or (nums[i] > r+1):
                miss = r+1
                count += 1
                r += miss
            else:
                r += nums[i]
                i += 1

        return count

s = Solution()
test = [1,2,31,33]
n = 2147483647

print "result for ",test," and ",n," is:"
print s.minPatches(test,n)
