DEBUG = True
def log(s):
    if DEBUG:
        print s

class Solution:
    def answer(self, s):
    	d = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    	romans = list(s)
    	value = 0
    	prev = 5000
    	for r in romans:
    		# Not in descending order,reduce the previous
    		if d[r] > prev:
    			value = value - prev*2
    		value += d[r]
    		prev = d[r]
    	return value	

# Testing
s = Solution()
test = "MMMMCMXCIX"
print "Tesing: ",test
print "Answers: ",s.answer(test) 
                
                 
