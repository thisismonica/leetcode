def compute(nums1, nums2, op):
        if op == "+":
            return nums1 + nums2
        if op == "-":
            return nums1 - nums2
        if op == "*":
            return nums1 * nums2
            
def tokenize(rpn):
    i = 0
    tokens = []
    while i < len(rpn):
        if rpn[i].isdigit():
            j = i+1
            while j < len(rpn) and rpn[j].isdigit():
                j += 1
            tokens.append(rpn[i:j])
            i = j
        else:
            tokens.append(rpn[i])
            i += 1
    
def evalRPN(rpn):
    nums = []
    tokens = tokenize(rpn)
    for token in rpn:
        if token in "+-*/":
            nums2, nums1 = nums.pop(), nums.pop()
            nums.append( compute( nums1, nums2, token) )
        else:
            nums.append(int(token))
    return nums[0]
    
class Solution(object):
    # RPN
    def addOperators1(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        if num == "":
            return []

        self.target = target
        self.res = []
        self.dfs1(num[0], num[0], [] ,num[1:])
        return self.res
    
    def dfs1(self, path, rpn, stack, num):
        if num == "":
            while stack:
                rpn += stack.pop()
            if evalRPN(rpn) == self.target:
                self.res.append(path)
            return
        
        stack1 = stack[:]
        rpn1 = rpn[:]
        while stack1 and stack1[-1] == "*":
            rpn1 += stack1.pop()
            
        self.dfs1(path + "+" + num[0], rpn1 + num[0], stack1 + ["+"], num[1:])
        self.dfs1(path + "-" + num[0], rpn1 + num[0], stack1 + ["-"], num[1:])
        self.dfs1(path + "*" + num[0], rpn + num[0], stack + ["*"], num[1:])
        self.dfs1(path + num[0], rpn + num[0], stack, num[1:])

    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        if num == "":
            return []

        self.target = target
        self.res = []
        self.dfs(0, "", num)
        return self.res
    
    def dfs(self, pos, path, num):
        if pos == len(num):
            if eval(path) == self.target:
                self.res.append(path)
            return
        
        for i in range(pos, len(num)):
            if i == len(num)-1:
                self.dfs(i+1, path + num[pos:i+1], num)
            else:
                self.dfs(i+1, path + num[pos:i+1]+ "+", num)
                self.dfs(i+1, path + num[pos:i+1] + "-", num)
                self.dfs(i+1, path + num[pos:i+1] + "*", num) 

    def addOperators2(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        def isLeadingZeros(num):
            return num.startswith('00') or int(num) and num.startswith('0')
        def solve(num, target, mulExpr = '', mulVal = 1):
            ans = []
            #remove leading zeros
            if isLeadingZeros(num):
                pass
            elif int(num) * mulVal == target:
                ans += num + mulExpr,
            for x in range(len(num) - 1):
                lnum, rnum = num[:x+1], num[x+1:]
                #remove leading zeros
                if isLeadingZeros(rnum):
                    continue
                right, rightVal = rnum + mulExpr, int(rnum) * mulVal
                #op = '+'
                for left in solve(lnum, target - rightVal):
                    ans += left + '+' + right,
                #op = '-'
                for left in solve(lnum, target + rightVal):
                    ans += left + '-' + right,
                #op = '*'
                for left in solve(lnum, target, '*' + right, rightVal):
                    ans += left,
            return ans
        if not num:
            return []
        return solve(num, target) 

    def addOperators3(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        if num == "":
            return []
        return self.dfs3(num, target)

    def dfs3(self, num, target, leftMultExpr="", multVal=1):
        res = []
        if (num == "0" or not num.startswith("0")) and int(num) * multVal == target:
            res.append(leftMultExpr + num)
                
        for i in range(1, len(num)):
            left = leftMultExpr + num[:i]
            # "+"    
            for expr in self.dfs3(num[i:], target - int(num[:i])*multVal):
                res.append(left + "+" + expr)
                
            # "-"
            for expr in self.dfs3(num[i:], int(num[:i])*multVal - target):
                res.append(left + "-" + expr)
            
            # "*"
            for expr in self.dfs3(num[i:], target, left + "*", int(num[:i])*multVal):
                res.append(expr)
        return res    
        
test = "123456789"
target = 45
s = Solution()
sol2 = s.addOperators2(test, target)
sol3 = s.addOperators3(test, target)
sol2.sort()
sol3.sort()
print sol2
print "***********************"
print sol3
'''
for i in range(len(sol2)):
    if sol2[i] != sol3[i]:
        print "sol2[i]: ", sol2[i]
        print "sol3[i]: ", sol3[i]
'''

