class Solution:
        # @param {string} s
            # @param {string} t
                # @return {boolean}
                    def isAnagram(self, s, t):
                                ls = list(s)
                                        ls.sort()
                                                lt = list(t)
                                                        lt.sort()
                                                                
                                                                        return ''.join(ls) == ''.join(lt)
