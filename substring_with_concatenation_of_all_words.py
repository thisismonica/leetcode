DEBUG = True
def log(s):
    if DEBUG:
        print s
import copy
class Solution:
    def findSubstring(self, S, L):
        if L == []:
            return []
        word_len = len(L[0])
        total_len = word_len * len(L)

        # Construct hash table
        d = {}
        for word in L:
            if word in d:
                d[word] += 1
            else:
                d[word] = 1

        # Traverse string
        res = []
        i = 0
        while i <= len(S)-total_len:
            curr = copy.copy(d)
            start = i
            while S[i:i+word_len] in curr and curr[ S[i:i+word_len] ] != 0:
                curr[ S[i:i+word_len] ] -= 1
                if curr[ S[i:i+word_len]]==0:
                    del curr[ S[i:i+word_len] ]
                i+=word_len
            if len(curr)==0:
                res.append( start )
            i = start+1
        return res


# Testing
s = Solution()
test1 = "abababab"
test2 = ["a","b","a"]
expect = [0,2,4]
print "Tesing: ",test1, test2
print "Expecting: ",expect
print "Answers: ",s.findSubstring(test1, test2)
                
                 
