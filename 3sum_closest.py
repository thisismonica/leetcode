DEBUG = True
def log(s):
    if DEBUG:
        print s
'''
Given an array S of n integers,
find three integers in S such that the sum is closest to a target number.
Return the sum of the three integers.
'''
class Solution:
    def answer(self, num, target):
        num.sort()
        res = sum( num[:3] ) # initial result

        # Iterate each value to find closest 3 sum
        for i, n in enumerate(num[:-2]):
            rest = target - n
            start = i+1
            end = len(num)-1
            closest_rest = num[start]+num[end]

            # Enumerate following array to find 2 sum closest
            while start < end:
                s = num[start]+num[end]
                if s < rest:
                    start += 1
                elif s > rest:
                    end -=1
                else:
                    # Find exact target sum
                    return target

                # Update cloest rest
                if abs(s-rest)< abs(closest_rest-rest):
                    closest_rest = s

            # Update closest 3 sum
            sum3 = closest_rest + n
            if abs(sum3-target)<abs(res-target):
                res = sum3
        return res 

        # O(n^3) solution
        '''
        def two_sum_closest( num, target):
            res = num[:2]
            for i,n in enumerate(num[:-1]):
                rest = target - n
                cloest_one = num[i+1]
                for m in num[i+1:]:
                    if abs(m-rest) < abs(cloest_one-rest):
                        cloest_one = m
                if abs(cloest_one+n - target) < abs(sum(res)-target):
                    res = [cloest_one , n]
            return res

        closest_val = sum(num[:3])
        for i in range(len(num)-2):
            rest = target - num[i]

            # Search the following array that has 2 sum closest to rest
            n1, n2 = two_sum_closest( num[i+1:], target )
            
            # Update cloest value
            if abs(n1+n2+num[i] - target) < abs(closest_val-target):
                closest_val = n1+n2+num[i]
        return closest_val
        '''

# Testing
s = Solution()
test1 = [0,2,1,-3]
test2 = 1
print "Tesing: ",test1,test2
print "Answers: ",s.answer(test1,test2) 
