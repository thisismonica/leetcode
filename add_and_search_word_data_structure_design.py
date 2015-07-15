class Node:
    def __init__(self, char):
        self.char = char
        self.children = {}
        self.end = False

class WordDictionary:
    
    def __init__(self):
        self.root = Node('')
    
    # @param {string} word
    # @return {void}
    # Adds a word into the data structure.
    def addWord(self, word):
        node = self.root
        for c in word:
            if c in node.children:
                node = node.children[c]
            else:
                node.children[c] = Node(c)
                node = node.children[c]
        node.end = True

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the data structure. A word could
    # contain the dot character '.' to represent any one letter.
    def search(self, word):
        queue = [ ( 0, self.root) ]
        while queue != []:
            (i, node) = queue.pop(0)
            if node.end and i==len(word):
                return True
            if i != len(word):
                if word[i] == ".":
                    for n in node.children.values():
                        queue.append( (i+1,n) )
                elif word[i] in node.children:
                    queue.append( (i+1, node.children[word[i]]) )

        return False

# Your WordDictionary object will be instantiated and called as such:
wordDictionary = WordDictionary()
wordDictionary.addWord("a")
wordDictionary.addWord("predispute")
wordDictionary.addWord("predisplay")

print "True: ",wordDictionary.search("a")
print "True: ",wordDictionary.search("p.....p...")
