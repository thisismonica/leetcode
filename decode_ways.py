class Solution:
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
        def isValid( s ):
            try:
                num = int(s)
            except ValueError:
                return False
            if len(s) == 1:
                return num != 0
            elif len(s) == 2:
                return num >=10 and num <=26
            else:
                return False
    
        if len(s) == 0:
            return 0
        dp0 = 1 if isValid(s[0]) else 0
        if len(s) == 1:
            return dp0
        
        # Calculate dp1 based on dp0
            # Case0: 12
        if isValid(s[1]) and isValid(s[0]+s[1]):
            dp1 = dp0 + 1
            # Case1: 27
        elif isValid(s[1]) and not isValid(s[0]+s[1]):
            dp1 = dp0
            # Case2: 20
        elif not isValid(s[1]) and isValid(s[0]+s[1]):
            dp1 = dp0
        else:
            dp1 = 0

        # DP
        for i in range(2, len(s) ):
            if isValid( s[i] ) and isValid( s[i-1]+s[i] ):
                dp = dp0 + dp1
            elif isValid( s[i] ) and not isValid( s[i-1]+s[i] ):
                dp = dp1
            elif not isValid( s[i] ) and isValid( s[i-1]+s[i] ):
                dp = dp0
            else:
                return 0
            dp0 = dp1
            dp1 = dp
                
        return dp1


# Testing

s = Solution()
line = '101'
print "Tesing: ",line
print "Answers: ",s.numDecodings(line)
