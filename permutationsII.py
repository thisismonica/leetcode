DEBUG = True
def log(s):
    if DEBUG:
        print s

class Solution:
    def permuteUnique(self, num):
        if len(num) == 1:
            return [num]
        visited = set()
        res = []
        for i in range(len(num)):
            if num[i] not in visited:
                visited.add(num[i])
                for comb in self.permuteUnique(num[:i]+num[i+1:]):
                    elem = [ num[i] ] + comb
                    res.append(elem)
        return res
# Testing
s = Solution()
test = [1,1,2]
expect = [[1,1,2],[1,2,1],[2,1,1]]
print "Tesing: ",test
print "Expecting: ",expect
print "Answers: ",s.permuteUnique(test) 
                
                 
