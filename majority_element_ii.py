class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def majorityElement(self, nums):
        candidates = {}
        for n in nums:
            if n in candidates:
                candidates[n] += 1
            elif len(candidates) < 2:
                candidates[n] = 1
            else:
                for k in candidates.keys():
                    if candidates[k] == 1:
                        del candidates[k]
                    else:
                        candidates[k] -= 1
        res = []
        for k in candidates.keys():
            if nums.count(k) > len(nums)/3:
                res.append(k)
        return res