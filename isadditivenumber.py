class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        def check(n1, n2, num):
            i = 0
            while i < len(num):
                sums = n1+n2
                i1 = i + len(str(sums))
                if num[i:i1] != str(sums):
                    return False
                i = i1
                n1 = n2
                n2 = sums
            return True
            
        for i in range(len(num)-2):
            number1 = int(num[:i+1])
            
            if num[i+1] == '0':
                if check(number1, 0, num[i+2:]):
                    return True
            else:
                for j in range(i+1, len(num)-1):
                    number2 = int(num[i+1:j+1])
                    if check(number1, number2, num[j+1:]):
                        return True
        return False


                

test = "1023"
s = Solution()
print s.isAdditiveNumber(test)