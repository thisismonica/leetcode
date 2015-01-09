DEBUG = True
def log(s):
    if DEBUG:
        print s

class Solution:
    '''
    Given an unsorted array of integers,
    Find the length of the longest consecutive elements sequence.
    '''
    def answer(self, num):
        # hash table for each value of num
        d = {}
        for n in num:
            d[n] = 1
            
        max_len = 1
        # iterate array for longest
        for n in num:
            if n in d:
                length = 1
                # Search consecutive value smaller than n
                number = n-1
                while number in d:
                    # Find 1 consecutive value, delete to avoid duplicate 
                    del d[number]
                    number -= 1
                    length += 1

                # Search consecutive value larger than n
                number = n+1
                while number in d:
                    del d[number]
                    number += 1
                    length +=1
                
                # Update max length
                max_len = max(max_len, length)
        return max_len

# Testing
s = Solution()
test = [0,3,7,2,5,8,4,6,0,1]
print "Tesing: ",test
print "Answers: ",s.answer(test) 
                
                 
