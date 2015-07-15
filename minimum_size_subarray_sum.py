class Solution:
    # @param {integer} s
    # @param {integer[]} nums
    # @return {integer}
    def minSubArrayLen(self, s, nums):
        left, right = 0,0
        sum = 0
        minWin = len(nums)
        
        while True:
            print "right: ",right," left: ",left
            print "sum: ",sum
            if sum < s:
                if right == len(nums):
                    if left==0:
                        return 0
                    break
                sum += nums[right]
                right += 1
            else:
                if left > right:
                    break
                minWin = min(minWin, right-left)
                sum -= nums[left]
                left += 1

        return minWin

s = Solution()
print s.minSubArrayLen(4,[1,4,4])

