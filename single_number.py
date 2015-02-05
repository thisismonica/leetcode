class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        xor_sum = 0
        for num in A:
            xor_sum ^= num
        return xor_sum