__author__ = 'monica_wang'
'''
given "word" as input
['word', '1ord', '1o1d', '1or1', '1o2', 'w1rd', 'w1r1', 'wo1d', 'wor1', '2r1', '2rd', '2r1', 'w2d', 'wo2', '3d', 'w3']

["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]

'''

class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        def translate(word, bit):
            word1 = list(word)

            bit1 = 1
            for i in range(len(word)):
                if bit1 & bit != 0:
                    word1[i] = '1'
                else:
                    word1[i] = word[i]
                bit1 <<= 1
            word2 = ""
            i = 0
            while i < len(word1):
                j = i
                while j< len(word1) and word1[j] == '1':
                    j += 1
                if j > i:
                    word2 += str(j-i)
                    i = j
                else:
                    word2 += word1[i]
                    i += 1
            return word2


        result = []

        N = len(word)
        for bit in range(2**N):
            wordT = translate(word,bit)
            result.append(wordT)

        return result



s = Solution()
test = "word"
print "result for ",test," is:"
print s.generateAbbreviations(test)