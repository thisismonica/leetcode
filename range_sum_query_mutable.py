class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        1, 3, 5
        [1, 4, 9]
        sumRange(0, 2) = sumArray[2] - sumArray[0] + array[0]
        update(i, val)
        update(1, 2) =
        1, 2, 5
        [1, 3, 8]
        """
        self.array = [0] * len(nums)
        self.bit = [0] * len(nums)

        for i in range(len(nums)):
            self.update(i, nums[i])

        self.array = nums[:]

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        diff = val - self.array[i]
        self.array[i] = val
        while i >= 0 and i < len(self.bit):
            self.bit[i] += diff
            i = self.getRightParent(i+1) - 1

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        res = self.array[i]
        while j >= 0 and j < len(self.bit):
            res += self.bit[j]
            j = self.getLeftParent(j+1) -1

        while i >= 0 and i < len(self.bit):
            res -= self.bit[i]
            i = self.getLeftParent(i+1) - 1
        return res

    def getLeftParent(self, n):
            '''
            :param n:
            :return: n after removing rightmost 1

            Example
                Node 7: 111 xor 001 110
                Node 6: 110 xor 010  100
                Node 4: 100
            '''
            #return n ^ (~ n + 1) -1
            return n - (n & (-1*n))

    def getRightParent(self, n):
            '''
            :param n:
            :return: n after removing rightmost 1

            Example
                1: 001 -> 110+1 = 111 -> 110 -> 001+1 = 010
                2: 010 -> 101+1 = 110 -> 100 -> 011+1 = 100
                3: 011 -> 100 + 1 = 101 -> 100 ->
                4: 100

            '''
            completeParent = self.getLeftParent(-1*n)
            return -1*completeParent


# Your NumArray object will be instantiated and called as such:
nums = [1,2,3]
print nums
numArray = NumArray(nums)

print numArray.sumRange(0, 1)

numArray.update(1, 10)
print numArray.sumRange(1, 2)
