DEBUG = True
def log(s):
    if DEBUG:
        print s

class Solution:
    def answer(self, num):
    	d = {1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M'}
        roman = ""
        order = 1
        while num>0:
            res = ""
            digit = num%10
            if digit < 4:
                res += d[order]*digit
            elif digit == 4:
                res = res + d[order] + d[order*5]
            elif digit > 4 and digit < 9:
                res = res + d[order*5] +d[order]
            else:
                res = res + d[order] + d[order*10]
            roman = res + roman
            num = num/ 10
            order *= 10
        return roman


# Testing
s = Solution()
test = 6
print "Tesing: ",test
print "Answers: ",s.answer(test) 
                
                 
