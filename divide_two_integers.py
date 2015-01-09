DEBUG = True
def log(s):
    if DEBUG:
        print s

class Solution:
        # Answer = dividend / divisor
    def answer(self, dividend, divisor):
        sign = 1
        if dividend < 0: sign *= -1
        if divisor < 0: sign *= -1
        divisor, dividend = abs(divisor), abs(dividend)
        if divisor > dividend: return 0

        # Using '<< 1' as multiply by 2
        exponent2 = 1
        shift_left = divisor
        while (shift_left << 1) <= dividend:
            shift_left <<= 1
            exponent2 = exponent2 << 1
 
        # Calculating the rest by recursion
        res = exponent2 + self.answer(dividend-shift_left, divisor) 
        
        # Check if overflow
        if sign == 1:
            return min(2147483647, res)
        else:
            return -1* min(2147483648, res)

# Testing
s = Solution()
test1 = 200
test2 = 3
print "Tesing: ",test1, test2
print "Answers: ",s.answer(test1, test2) 
                
                 
