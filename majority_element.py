DEBUG = True
def log(s):
    if DEBUG:
        print s

class Solution:

    # Find the majority element, occurs more than floor(n/2) times
    def answer(self, num):
        occurances = {}
        for n in num:
            if n not in occurances:
                occurances[n] = 1
            else:
                occurances[n] += 1
                if occurances[n] > len(num)/2:
                    return n

# Testing
s = Solution()
test = [4]
print "Tesing: ",test
print "Answers: ",s.answer(test) 
                
                 
