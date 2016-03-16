class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        res = ""
        for s in strs:
            es = ""
            for i in range(len(s)):
                if s[i] != '0' and s[i] != '^':
                    es += s[i]
                else:
                    es += '^'
                    es += s[i]
            es += '0'
            res += es
        return res
        

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        strs = []
        str = ""
        trans = False
        for i in range(len(s)):
            if trans:
                str += s[i]
                trans = False
            elif s[i] == '^':
                trans = True
            elif s[i]=='0':
                strs.append(str)
                str=""
            else:
                str += s[i]
        return strs
        

# Your Codec object will be instantiated and called as such:
codec = Codec()
strs = ['abc','$%^']
print codec.decode(codec.encode(strs))
