class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        # num with less than 3 digits
        def n2w(num):
            d1 = { 0: '', 1:'One',2:'Two',3:'Three',4:'Four',5:'Five', 6:'Six', 7:'Seven', 8:'Eight', 9:'Nine'}
            d11 = {10:'Ten', 11:'Eleven', 12:'Twelve', 13:'Thirteen', 14:'Fourteen', 15:'Fifteen', 16:'Sixteen', 17:'Seventeen', 18:'Eighteen', 19:'Nineteen' }
            d2 = { 0: '', 2:'Twenty', 3:'Thirty', 4:'Fourty', 5:'Fifty', 6:'Sixty', 7:'Seventy', 8:'Eighty', 9:'Ninety'}
            
            res = []
            digits = []
            while num:
                digits.append(num%10)
                num /= 10
            
            for i in range(len(digits)):
                if i == 0:
                    res.append(d1[digits[i]])
                elif i == 1:
                    if digits[i] == 1:
                        res[-1] = d11[10 + digits[i-1]]
                    else:
                        res.append(d2[digits[i]])
                elif i == 2:
                    res.append('Hundred')
                    res.append(d1[digits[i]])

            print "result: ", res
            return " ".join(res[::-1])
            
        if num == 0:
            return "Zero"
        d = ["", "thousand", "million", "billion"]
        res = []
        i = 0
        while num:
            num3d = num % 1000
            print "num3d: ",num3d
            res.append(d[i])
            res.append(n2w(num3d))
            i += 1
            num /= 1000
        
        return " ".join(res[::-1])
                    
                        
test = 201
s=Solution()
print s.numberToWords(test)