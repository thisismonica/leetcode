class Solution:
    # @param {integer[]} height
    # @return {integer}
    def largestRectangleArea(self, height):
        i = 0
        stack = []
        max_rect = 0
        height = [0]+height+[0]
        
        while i < len(height):
            print "stack: ",stack
            if stack == []:
                stack.append(i)
                i+=1
            else:
                if height[i] >= height[ stack[-1] ]:
                    stack.append(i)
                    i+=1
                else:
                    j = stack.pop()
                    left = stack[-1]
                    max_rect = max(max_rect, height[j]*(i-left-1))
                    print "max_rect: ",max_rect
        return max_rect

s = Solution()
test = [1]
print "Test: ",test
print "Answer: ",s.largestRectangleArea(test)
