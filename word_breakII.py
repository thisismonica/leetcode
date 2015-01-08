class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a list of strings
    def wordBreak(self, s, dict):
        if len(s) == 0:
            return []
        i = 0
        res = []
        
        possible = False
        for i in range( len(s) ):
            if s[i:] in dict:
                possible = True
                break
        if not possible:
            return res
        
        for i in range(1, len(s)+1):
            if s[:i] in dict:
                for r in self.wordBreak(s[i:],dict):
                    res.append(s[:i]+" "+r)
                if i == len(s):
                    res.append(s)
        return res