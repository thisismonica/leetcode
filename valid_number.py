class Solution:
    # @param s, a string
    # @return a boolean
    def isNumber(self, s):
        # State type:
        # 0: nothing        [0,1,3,-1,2,-1]
        # 1: digit(s)       [8,1,-1,5,4,-1]
        # 2: dot            [-1,4,-1,-1,-1,-1]
        # 3: sign           [-1,1,-1,-1,2,-1]
        # 4: digit, dot     [8,4,-1,-1,-1,-1]
        # 5: e              [-1,6,7,-1,-1,-1]
        # 6: e digit        [8,6,-1,-1,-1,-1]
        # 7: e sign         [-1,6,-1,-1,-1,-1]
        # 8: end            [8,-1,-1,-1,-1,-1]
        
        # Input type:
        # space(0):
        # digit(1):
        # sign(2):
        # e(3):
        # dot(4):
        # others(5):
        table = [ [0,1,3,-1,2,-1], [8,1,-1,5,4,-1], [-1,4,-1,-1,-1,-1],[-1,1,-1,-1,2,-1],[8,4,-1,5,-1,-1],[-1,6,7,-1,-1,-1],[8,6,-1,-1,-1,-1], [-1,6,-1,-1,-1,-1], [8,-1,-1,-1,-1,-1] ]
        state = 0
        for i in range( len(s) ):
            if s[i] == ' ': state = table[state][0]
            elif s[i].isdigit(): state = table[state][1]
            elif s[i]=='+' or s[i]=='-': state = table[state][2]
            elif s[i]=='e' or s[i]=='E': state = table[state][3]
            elif s[i]=='.': state = table[state][4]
            else: state = table[state][5]
            if state == -1:
                return False
        if state == 8 or state == 1 or state == 4 or state==6:
            return True
        else:
            return False