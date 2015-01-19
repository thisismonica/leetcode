DEBUG = True
def log(s):
    if DEBUG:
        print s

class Solution:
    # It's all about customized sorting
    def answer(self, num):
        # Define customized compare function for sorting 
        def compare(n1, n2):
            if n1+n2 > n2+n1:
                return 1
            elif n1+n2 < n2+n1:
                return -1
            else:
                return 0

        num_str = [str(n) for n in num]
        res = ""

        # Sorting according to customized function
        for n in reversed( sorted(num_str,cmp=compare) ):
            res += n

        '''
        num_str = [str(n) for n in num]
        max_len = max( [len(n) for n in num_str] )
        d = {}

        # Extend each number to reach same length
        for n in num_str:
            if len(n) < max_len:
                last = list(n)[-1]
                k =int( n+ last*(max_len-len(n)) )
                if k in d:
                    d[k] += n
                else:
                    d[k] = n
            else:
                if int(n) in d:
                    d[int(n)] += n
                else:
                    d[int(n)] = n

        # Sort dict by key
        res = ""
        for key in reversed(sorted(d.keys() )):
            res += d[key]
        '''

        # Remove unnecessary zeros in head
        res_list = list(res)
        i = 0
        while res_list[i] == '0' and i != len(res)-1:
            i += 1
        res_list = res_list[i:]

        return ''.join( res_list)

# Testing
s = Solution()
test = [12,121]
expect = "12121"
print "Tesing: ",test
print "Expecting: ",expect
print "Answers: ",s.answer(test) 
