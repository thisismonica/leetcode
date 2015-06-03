class TrieNode:
    # Initialize your data structure here.
    def __init__(self, word):
        self.word = word
        self.children = {}
        self.val = 0
class Trie:
    def __init__(self):
        self.root = TrieNode('')
    
    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    def insert(self, word):
        node = self.root
        for i in range( len(word) ):
            if word[:i+1] in node.children:
                node = node.children[ word[:i+1] ]
            else:
                ch = TrieNode(word[:i+1])
                node.children[word[:i+1]]  = ch
                node = ch
        node.val = 1
    
    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the trie.
    def search(self, word):
        node = self.root
        for i in range( len(word) ):
            if word[:i+1] not in node.children:
                return False
            node = node.children[ word[:i+1] ]
        return node.val==1
    
    # @param {string} prefix
    # @return {boolean}
    # Returns if there is any word in the trie
    # that starts with the given prefix.
    def startsWith(self, prefix):
        node = self.root
        for i in range( len(prefix) ):
            if prefix[:i+1] not in node.children:
                return False
            node = node.children[ prefix[:i+1] ]
        return True