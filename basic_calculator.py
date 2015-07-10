class Solution:
    # @param {string} s
    # @return {integer}
    def calculate(self, s):
        
        numbers = []
        signs = []
        i = 0
        
        while i < len(s) :
            if s[i].isdigit():
                j = i+1
                while j< len(s) and s[j].isdigit():
                    j += 1
                num = int( s[i:j] )
                numbers.append( num )
                i = j
                continue
            
            if s[i] in "+-(":
                signs.append(s[i])
        
            # Calculation
            elif s[i] == ")":
                
                sign = signs.pop()
                inner_signs = []
                inner_nums = [ numbers.pop() ]
                
                while sign != "(":
                    inner_signs.append( sign )
                    sign = signs.pop()
                    inner_nums.append( numbers.pop() )
                
                res = inner_nums[-1]
                for j in reversed(range(len(inner_nums)-1)):
                    res = res + inner_nums[j] if inner_signs[j]=='+' else res-inner_nums[j]
                numbers.append( res )
            
            i += 1
                
        if numbers == []:
            return 0
                        
        res = numbers[0]
        for i in range( 1, len(numbers) ):
            res = res + numbers[i] if signs[i-1]=='+' else res-numbers[i]
        return res



s = Solution()
print s.calculate("(4)");
