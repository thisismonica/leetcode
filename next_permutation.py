class Solution:
    # @param num, a list of integer
    # @return a list of integer
    
    def nextPermutation(self, num):
        if len(num) <=1 : return num
        if num == sorted( num, reverse=True ): num.reverse(); return num
        
        # right->left Find partition number violates ascending order
        N = len(num)
        j = N-1
        prev = N-2
        while prev >= 0 and num[prev]>=num[j]:
            prev = prev-1
            j = j-1
        partition = prev
        j = N-1
        while j>0 and num[j] <= num[partition]:
            j = j-1
        change = j
        
        
        # Swap partition, change
        tmp = num[partition]
        num[partition] = num[change]
        num[change] = tmp
        
        # Keep the rest des
        num = num[:partition] + [ num[partition] ] + num[partition+1:][::-1]
        
    return num