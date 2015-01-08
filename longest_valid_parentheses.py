DEBUG = True
def log(s):
    if DEBUG:
        print s

class Solution:
    def answer(self, s):
        dp = [0 for i in range(len(s)+1)]
        dp[0] = 0

        for i in range(1, len(s)+1):
            if s[i-1] == '(':
                dp[i] = dp[i-1] - 1
            elif s[i-1] == ')':
                dp[i] = dp[i-1] + 1

        # Between 2 identical values of dp is the valid parenthesis
        # Find the longest distance between 2 identical values
        left_pos = {} # dict: key= dp, value= dp pos
        right_pos = {}
        for pos, value in enumerate(dp):
            if value in right_pos:
                right_pos[value] = pos
            else:
                right_pos[value] = pos
                left_pos[value] = pos
        max_distance = 0
        for v in right_pos:
            max_distance =max(max_distance, right_pos[v] - left_pos[v])
        return max_distance
# Testing
s = Solution()
test = ")()())"
print "Tesing: ",test
print "Answers: ",s.answer(test) 
                
                 
