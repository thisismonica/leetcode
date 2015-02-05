class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, l):
        if l==[]:
            return 0

        local_max, local_min = None, None
        max_product = l[0]
        
        for num in l:
            if num > 0:
                local_max = local_max * num if local_max else num
                local_min = local_min*num if local_min else None
            elif num == 0:
                local_max, local_min = None, None
            else:
                prev_max = local_max
                local_max = local_min*num if local_min else None
                local_min = prev_max*num if prev_max else num
                
            max_product = max(max_product, local_max, num)
        return max_product
            