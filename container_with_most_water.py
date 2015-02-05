class Solution:
    # @return an integer
    def maxArea(self, height):
        L, R, maxV = 0, len(height) - 1, -1
        while L < R:
            maxV = max(maxV, min( height[L], height[R] ) * (R - L) )
            if height[L] <= height[R]:
                L += 1
            else:
                R -= 1
        return maxV