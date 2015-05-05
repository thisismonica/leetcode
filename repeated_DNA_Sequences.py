DEBUG = True
def log(s):
    if DEBUG:
        print s

class Solution:
    def answer(self, s):
        mydict = {}
        length = 10
        result = []

        for i in range(len(s)):
            if s[i:i+10] in mydict:
                mydict[ s[i:i+10] ] += 1
                if mydict[ s[i:i+10] ] == 2:
                    result.append( s[i:i+10] )
            else:
                mydict[ s[i:i+10] ] = 1
        return result   

# Testing
s = Solution()
test1 = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
test2 = ["AAAAACCCCC","CCCCCAAAAA"]
print "Tesing: ",test1
print "Answers: ",s.answer(test1) , "Expecting: ", test2
