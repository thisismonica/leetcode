DEBUG = True
def log(s):
    if DEBUG:
        print s

class Solution:
    def answer(self, s):

        s = list(s)
        idx = (0,0)
        max_len = 1
        i = 0
        while i< len(s):
            # Check for duplicate characters
            j = i
            while j+1<len(s) and s[j+1] == s[i]:
                j+=1
            if j-i+1 >max_len:
                max_len = j-i+1
                idx = (i,j)
            i = (j+i)/2

            # i as center for odd length palindrome
            left, right = i, i
            while left-1>=0 and right+1<=len(s)-1:
                if s[left-1]!=s[right+1]:
                    break
                left,right = left-1, right+1
                
            if right-left+1 > max_len:
                max_len = right-left+1
                idx = (left,right)
            
            # i as center for even length palindrome
            if i<len(s)-1 and s[i+1] == s[i]:
                left, right = i, i+1
                while left-1>=0 and right+1<=len(s)-1:
                    if s[left-1]!=s[right+1]:
                        break
                    left,right = left-1, right+1
                if right-left+1 >max_len:
                    max_len = right-left+1
                    idx = (left,right)
            i+=1
            
        return "".join( s[idx[0]:idx[1]+1] )
                
# Testing
s = Solution()
test = "ccc"
expect = "ccc"
print "Tesing: ",test
print "Answers: ",s.answer(test) 
