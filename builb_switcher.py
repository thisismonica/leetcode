__author__ = 'monica_wang'
class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """

        '''
        for bulb i, i is on if number of factors of i is odd
        i is off if number of factors of i is even.

        Factors appear in pairs.
        Perfect squares has odd number of factors.
        '''
        i = 0
        while i*i <=n:
            i += 1
        return i-1