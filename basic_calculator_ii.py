class Solution:
    # @param {string} s
    # @return {integer}
    def calculate(self, s):
        num_stack = []
        op_stack = []
        i = 0
        
        while i< len(s):
            if s[i] == ' ':
                i += 1
            elif s[i] in ['+','-','*','/']:
                op_stack.append( s[i] )
                i += 1
            else:
                j = i
                while( i<len(s) and s[i].isdigit() ):
                    i+=1
                curr = int( s[j:i] )
                res = curr
                if op_stack!=[] and op_stack[-1] in ['*','/']:
                    op = op_stack.pop()
                    prev = num_stack.pop()
                    res = curr*prev if op=='*' else prev/curr
                    num_stack.append(res)
                else:
                    num_stack.append( curr )
    
        res = num_stack[0]
        for i in range(1, len(num_stack) ):
            res = res + num_stack[i] if op_stack[i-1]=='+' else res - num_stack[i]
return res