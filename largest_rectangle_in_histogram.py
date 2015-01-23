class Solution:
    # @param height, a list of integer
    # @return an integer
    def largestRectangleArea(self, height):
        # Add last height as 0 to make the last part works as left part > right
        height.append( 0 )

        # Algorithm: iterate each bar to calculate the area of its control rectangle
        # Definition: control rectangle of bar: the bar is the highest bar in the rectangle
        stack = []
        i = 0
        maxArea = 0
        while i < len(height):
            print "\ni: ",i, "stack: ",stack

            # Push stack for bars with ascending heights
            if stack==[] or height[ stack[-1] ] <= height[i]:
                stack.append( i )
                i = i+1

            '''
            Pop bar as current bar and calculate control rectangle
            Control rectangle: height = height of current top bar
            Width: for the current bar the left boundary is i since height[i]<height[bar] 
                and right boundary is stack top since height of stack top is heigher
                right boundary is 0 if stack is empty
            '''
            else:
                curr_bar = stack.pop()
                if stack!=[]:
                    area = height[curr_bar] * (i - stack[-1] -1)
                else:
                    area = height[curr_bar] * (i)
                maxArea = max(maxArea, area)
                print "area: ",area
 
        return maxArea
s = Solution()
test1 = [4,3]
expect = 6
print "Testing: ",test1
print "Expecting: ",expect
print "Answer: ", s.largestRectangleArea(test1)