import re
class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        
        if re.match("^-", s):
            sign = "-"
            s = s[1:]
            
        intp = r"[0-9]+"
        decp = r"(?P<int>[0-9]+)?\.(?P<dec>[0-9]*[1-9]$)"
        ep = r"(?P<int>[0-9]+)e(?P<power>[0-9]+)"

        intmatch = re.match(intp, s)
        decmatch = re.match(decp, s)
        ematch = re.match(ep, s)
        
        if intmatch and intmatch.begin()== 0 and intmatch.end() == len(s)-1:
            print "it's integer"
            print intmatch.group(0)
            return True
        if decmatch and decmatch.begin()==0 and decmatch.end() == len(s)-1:
            print "its' decimal"
            print decmatch.groupdict()
            return True
        if ematch and ematch.begin() == 0  and ematch.end() == len(s)-1:
            print "it's e"
            print ematch.groupdict()
            return True
        return False

test = "0e"
s = Solution()
print s.isNumber(test)
