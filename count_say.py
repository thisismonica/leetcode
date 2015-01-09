class Solution:
    # @return a string
    def countAndSay(self, n):
        if n <= 0: return ""
        s = "1"
        if n == 1: return s
        
        i = 2
        while i < n+1:
            newStr = ""
            j = 0
            while j < len(s):
                num = s[j]
                j = j+1
                cnt = 1
                # count
                while j< len(s) and s[j]==num:
                    j = j+1
                    cnt = cnt+1
                # say
                newStr = newStr + str(cnt) + num
            s = newStr
            i = i+1
        return s

    # @return a string
    def countAndSayKitt(self, n):
        s = '1'
        for i in xrange(n-1):
            prev = newS = ''
            num = 0
            for curr in s:
                if prev != '' and prev != curr:
                    newS += str(num) + prev
                    num = 1
                else:
                    num += 1
                prev = curr
            newS += str(num) + prev
            s = newS
        return s
s = Solution()
n = 40
print "Answer for n= ", n, " is: "
print s.countAndSayKitt(n)
