class Solution:
    # @param {string} input
    # @return {integer[]}
    def diffWaysToCompute(self, input):
        nums,ops = self.parse(input)
        return self.diffWays(ops,nums)
    
    def diffWays(self, ops, nums):
        print nums,ops
        if len(nums) != len(ops)+1:
            return []
        if len(ops)==0:
            return [nums[0]]
        if len(ops)==1:
            return [ self.cal(ops[0], nums[0],nums[1])]
        ans = []
        for i in range(len(ops)):
            res = self.cal(ops[i],nums[i],nums[i+1])
            ans.extend( self.diffWays( ops[:i]+ops[i+1:], nums[:i]+[res]+nums[i+2:]) )
        return ans
    
    def cal(self,op, n1, n2):
        if op=='+':
            return n1+n2
        if op=='-':
            return n1-n2
        if op=='*':
            return n1*n2

    def parse(self, s):
        i = 0
        nums = []
        ops = []
        while i<len(s):
            if s[i]==' ':
                i+=1
            if s[i].isdigit():
                j = i
                while j<len(s) and s[j].isdigit():
                    j+=1
                nums.append( int(s[i:j]) )
                i = j
            elif s[i] in '+-*':
                ops.append(s[i])
                i+=1
        return nums,ops
s=Solution()
print s.diffWaysToCompute("15-7*6+24")
