DEBUG = True
def log(s):
    if DEBUG:
        print s

import math
class Solution:
    '''
    Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

    Try to solve it in linear time/space.

    Return 0 if the array contains less than 2 elements.
    '''
    def answer(self, num):
        if len(num) <2:
            return 0

        # Application of Pigeonhole Principle
        max_val = max(num)
        min_val = min(num)

        # Initialize buckets
        n = len(num)
        buckets = [[] for i in range(n-1)]
        bucket_size = (max_val-min_val)/float( (n-1) )

        # Construct buckets for (n-2) numbers
        for number in num:
            if number == max_val or number == min_val:
                continue
            k = int( math.floor( (number - min_val)/bucket_size) )
            buckets[k].append(number)

        L = [] # non-empty buckets
        for b in buckets:
            if b!=[]:
                L.append( b )

        # According to Pigeon Principle, at least 1 bucket is empty
        # The maximum gap should be gap between 2 elements from 2 successive bucket
        # Initial max gap should be gap either between min-val and first non-empty bucket (minimum) or between max_val and last non-empty bucket
        if L==[]:
            return max_val - min_val
        max_gap = max(min(L[0])-min_val, max_val-max(L[-1]) )
        for i in range(1, len(L)):
            gap = min(L[i]) - max( L[i-1] )
            max_gap = max(max_gap, gap)
            
        return max_gap

# Testing
s = Solution()
test = [15252,16764,27963,7817,26155,20757,3478,22602,20404,6739,16790,10588,16521,6644,20880,15632,27078,25463,20124,15728,30042,16604,17223,4388,23646,32683,23688,12439,30630,3895,7926,22101,32406,21540,31799,3768,26679,21799,23740]
print "Tesing: ",test
print "Answers: ",s.answer(test) 
