import re
class Solution(object):
    def wordPatternMatch(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        self.dict1 = {}
        self.dict2 = {}
        return self.match(pattern, str)
        
    def match(self, pattern, str):
        tol = len(set(pattern))
        if tol > len(str):
            return False
        if tol == 0:
            return str == ""
        '''
        if tol == 1:
            if len(str)%len(pattern) != 0:
                return False
            k = len(str)/len(pattern)
            words = [ str[i:i+k] for i in range(len(str))[::k] ]
            if len(set(words)) == 1:
                if pattern[0] not in self.dict1 and words[0] not in self.dict2:
                    self.dict1[pattern[0]] = words[0]
                    self.dict2[words[0]] = pattern[0]
                    return True
                if pattern[0] not in self.dict1 or words[0] not in self.dict2:
                    return False
                if self.dict1[pattern[0]] == words[0] and self.dict2[words[0]] == pattern[0]:
                    return True
                return False
            return False
        '''
            
        # search substring to map pattern[0]
        for i in range(len(str)-tol+1):
            if pattern[0] in self.dict1 and str[:i+1] in self.dict2:
                if self.dict1[pattern[0]] == str[:i+1] and self.dict2[str[:i+1]] == pattern[0]:
                    if self.match(pattern[1:], str[i+1:]):
                        return True
            if pattern[0] not in self.dict1 and str[:i+1] not in self.dict2:
                self.dict1[pattern[0]] = str[:i+1]
                self.dict2[str[:i+1]] = pattern[0]
                if self.match(pattern[1:], str[i+1:]):
                    return True
                else:
                    del self.dict1[pattern[0]]
                    del self.dict2[str[:i+1]]
        return False
                
s = Solution()
pattern = "aba"
string = "xxxx"
print s.wordPatternMatch(pattern, string)           
        
        
            