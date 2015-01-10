DEBUG = True
def log(s):
    if DEBUG:
        print s

class Solution:
    '''
    Given a set of candidates numbers (C) and a target number (T), find all unique combinations in C where the candidates numbers sums to T.
    - All numbers positive
    - Elements in solution set should be non-descending
    - Repeated number from C is allowed
    C=[2,3,6,7], target = 7
    Answer = [2,2,3]
    '''
    
    def combinationSum(self, candidates, target):

        # Define help function for recursion
        # Assume candidates sorted and all less equal to target
        def help( candidates, target):
            if target == 0 or candidates == []:
                return []
            res = []

            # Iterate reversely to enumerate each combination
            for i in reversed( range(1, len(candidates)) ): 
                remaining = target - candidates[i]
                current = [ candidates[i] ]

                # combine (repeated) current cadidate with previous
                while remaining > 0:
                    for c in help(candidates[:i], remaining):
                        res.append( c + current )
                    remaining -= candidates[i]
                    current += [candidates[i]]

                # repeated current candidates
                if remaining == 0:
                    res.append(current)

            # First element: only when target%firstElememt == 0
            if target % candidates[0] == 0:
                res.append([candidates[0] for i in range(target/candidates[0]) ])
            return res


        candidates.sort()
        return help(candidates, target)


# Testing
s = Solution()
test1 = [2,3,5]
test2 = 7
print "Tesing: ",test1, test2
print "Answers: ",s.combinationSum(test1, test2) 
                
                 
