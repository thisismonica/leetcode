class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        reversed_str = ""
        j = len(s)
        while j>=0:
            i = s.rfind(' ',0,j)
            if i+1!=j:
                reversed_str += s[i+1:j]
                reversed_str += " "
            j = i
        return reversed_str[:-1]