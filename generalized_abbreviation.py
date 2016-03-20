__author__ = 'monica_wang'
'''
given "word" as input
['word', '1ord', '1o1d', '1or1', '1o2', 'w1rd', 'w1r1', 'wo1d', 'wor1', '2r1', '2rd', '2r1', 'w2d', 'wo2', '3d', 'w3']
['4', '3d', '2r1', '2rd', '1o2', '1o1d', '1or1', '1ord', 'w3', 'w2d', 'w1r1', 'w1rd', 'wo2', 'wo1d', 'wor1', 'word']

["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]

'''

class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        def dfs(word, pos):
            if pos == len(word):
                self.result.append(word)
                return

            if pos-1 >=0 and word[pos-1].isdigit():
                i = pos-1
                while i>=0 and word[i].isdigit():
                    i -= 1
                number = str(int(word[i+1:pos]) + 1)
                offset = (pos - i) - len(number)
                updatePos = pos + 1 - offset
                dfs(word[:i+1] + str(number) + word[pos+1:], updatePos)
            else:
                dfs(word[:pos] + '1' + word[pos+1:], pos+1)

            dfs(word[:], pos+1)

        self.result = []
        dfs(word, 0)
        return self.result



s = Solution()
test = "dictionary"
print "result for ",test," is:"
print s.generateAbbreviations(test)