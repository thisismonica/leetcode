DEBUG = True
def log(s):
    if DEBUG:
        print s
'''
# 1. Pad words in greedy approach
# 2. Each line has exactly L characters(include space)
# 3. Space between words should be distributed as evenly as possible
# 4. If not even, left has more spaces than right
# 5. Should not split words
# 6. Last line is left justified without extra spaces
'''
class Solution:
    def fullJustify(self, words, L):
        lines = []
        i = 0
        while i < len(words):
            # Calculate number of words in each line
            j = i
            total_len = 0 
            while j < len(words):
                total_len += (len(words[j] )+1)
                if total_len-1 > L:
                    break
                j += 1
            total_len -= 1  #Remove last space

            # Last line: left justification
            if j==len(words):
                s = " ".join(words[i:j])
                total_space = (L-total_len)
                s += " "*total_space
                lines.append( s )

           # Justify: Insert space accordingly
            else:
                print "j: ",j,"; total_len: ",total_len
                # Roll-back
                total_len -=  ( len(words[j]) + 1)
                j -= 1

                # Only 1 word in line
                if i==j: 
                    s = words[i]
                    s += (L-total_len)*" "
                    lines.append(s)
                    i += 1
                    continue

                num_space = (L-total_len)/(j-i) + 1
                num_extra_space = (L-total_len)%(j-i)
                s = ""
                for k in range(i,j):
                    s+=words[k]
                    s+=" "*num_space
                    if k < i+num_extra_space:
                        s+=" "
                s+=words[j]
                lines.append( s )
            i = j+1
        return lines

# Testing
s = Solution()
'''
test1 = ["This", "is", "an", "example", "of", "text", "justification."]
test2 = 16
expect = ["This    is    an","example  of text","justification.  "]
'''
test1 = ["a","b","c"]
test2 = 1
expect = ["a","b","c"]
print "Tesing: ",test1, test2
print "Expecting: ",expect
print "Answers: ",s.fullJustify(test1, test2) 
                
                 
