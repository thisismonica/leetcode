class Solution:
    # @return a string
    def fractionToDecimal(self, numerator, denominator):
        # Initializa result with sign
        if numerator*denominator < 0:
            sign_res = "-"
            numerator = abs( numerator )
            denominator = abs( denominator )
        else:
            sign_res = ""
        
        # Integer part
        int_res =  str( numerator/denominator )
        residual = numerator%denominator
        past_residual = {residual : 0}
        frac_res = []
        
        # Dividing and record residuals, Add parenthesis when meet recurring residual
        curr_pos = 0
        while residual != 0:
            frac_res.append( str((residual*10) / denominator) )
            residual = (residual*10) % denominator
            curr_pos = curr_pos+1
            
            # Recurring residual
            if residual in past_residual:
                left_pos = past_residual[residual]
                right_pos = curr_pos
                frac_res.insert(left_pos, "(" )
                frac_res.insert(right_pos+1, ")" ) # insert position updated by adding 1 since "(" inserted
                break
            else:
                past_residual[residual] = curr_pos
        frac_res = "".join( frac_res )

        # Output result
        if frac_res != "":
            res = sign_res + int_res + "." + frac_res
        else:
            res = sign_res + int_res
        return res

# Testing
s = Solution()
print "Answer to 6/5: ",s.fractionToDecimal(6,5)
