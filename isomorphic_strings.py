class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        ds = {}
        dt = {}
        for i in range(len(t)):
            if t[i] in dt:
                if dt[t[i]] != s[i]:
                    return False
            else:
                if s[i] in ds:
                    return False
                dt[t[i]] = s[i]
                ds[s[i]] = t[i]
        return True