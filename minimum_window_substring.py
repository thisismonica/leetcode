class Solution:
    # @param {string} s
    # @param {string} t
    # @return {string}
    def minWindow(self, s, t):
        left,right = 0,0
        i, j = 0, len(s)
        chars = {}
        for c in t:
            if c in chars:
                chars[c] += 1
            else:
                chars[c] = 1
        count = 0
        
        while True:
            if count != len(t):
                if right == len(s):
                    break
                if s[right] in chars:
                    chars[s[right]] -= 1
                    if chars[s[right]] >= 0:
                        count += 1
                right += 1
            else:
                if right < left:
                    break
                if right-left < j-i:
                    i,j = left,right
                if s[left] in chars:
                    chars[s[left]] += 1
                    if chars[s[left]] > 0:
                        count -= 1
                left += 1
    
        if right-left==len(s) and count != len(t):
            return ""
return s[i:j]


