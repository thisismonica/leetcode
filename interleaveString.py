class Solution:
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
	print "Entering isInterleave..."
	print "s1 is ",s1
	print "s2 is ",s2
	print "s3 is ",s3
	print "************************"
        if len(s3) != len(s1) + len(s2):
            return False
        if len(s3) == 0:
            return True
            
        p1, p2, p3 = 0,0,0
        
        while p3 != len(s3):
            if p1 == len(s1):
                if s3[p3] == s2[p2]: p2 = p2 + 1 ; p3 = p3 + 1; continue
                else: return False
            if p2 == len(s2):
                if s3[p3] == s1[p1] : p1 = p1 + 1 ; p3 = p3 + 1; continue
                else: return False
            if s3[p3] == s1[p1] and s3[p3] == s2[p2]:
                return self.isInterleave(s1[p1+1:], s2[p2:], s3[p3+1:]) or self.isInterleave(s1[p1:],s2[p2+1:],s3[p3:])
            elif s3[p3] == s1[p1]:
                p1 = p1 + 1
            elif s3[p3] == s2[p2]:
                p2 = p2 + 1
            else:
                return False
            p3 = p3 + 1
        return True

s = Solution()
s1 = "aa"
s2 = "ab"
s3 = "aaba"
print s.isInterleave(s1,s2,s3)
