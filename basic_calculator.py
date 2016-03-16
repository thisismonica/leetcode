class Solution:
    # @param {string} s
    # @return {integer}
    def calculate(self, s):
        return self.evalRPN( self.toRPN(s) )
    
    def evalRPN(self, rpn):
        nums = []
        for token in rpn:
            if token in "+-*/":
                nums2, nums1 = nums.pop(), nums.pop()
                nums.append( self.compute( nums1, nums2, token) )
            else:
                nums.append(int(token))
        return nums[0]
                
    def toRPN(self, s):
        i = 0
        rpn = []
        stack = []
        while i < len(s):
            if s[i].isdigit():
                j = i+1
                while j< len(s) and s[j].isdigit():
                    j += 1
                rpn.append( s[i:j] )
                i = j
                continue
            else:
                if s[i] in "+-*/":
                    while stack and self.getPriority( stack[-1] ) > self.getPriority( s[i] ):
                        rpn.append( stack.pop() )
                    stack.append( s[i] )
                elif s[i] == '(':
                    stack.append( s[i] )
                elif s[i] == ')':
                    while stack and stack[-1] != '(':
                        rpn.append( stack.pop() )
                    stack.pop()
            i += 1
        while stack != []:
            rpn.append( stack.pop() )
        return rpn
        
    def getPriority(self, sign):
        if sign in "+-":
            return 1
        if sign in "*/":
            return 2
        if sign in "(":
            return 0
        
    def compute(self, nums1, nums2, op):
        if op == "+":
            return nums1 + nums2
        if op == "-":
            return nums1 - nums2
        if op == "*":
            return nums1 * nums2
        if op == "/":
            return nums1 / nums2

s = Solution()
test = 
        
                
                
