class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if strs == []:
            return ""
        n = len(strs)
        i = 0
        minLen = min( [ len(s) for s in strs] )
        common = ""
        while i < minLen:
            ch = strs[0][i]
            for j in range(1,n):
                if strs[j][i] != ch:
                    return common
            common = common + ch
            i = i+1
        return common