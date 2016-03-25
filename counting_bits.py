class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        '''
        count[num] = count[num>>1] + (last bit is 1)
        '''

        count = [0] * (num+1)
        count[0] = 0

        for i in range(1, num+1):
            count[i] = count[i>>1]
            if i & 1 != 0:
                count[i] += 1
        return count

s = Solution()
num = 5
print s.countBits(num)