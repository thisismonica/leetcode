class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.children = {}
        self.end = False # end of word
    
    def insert(self, word):
        node = self
        for i in range( len(word) ):
            if word[i] not in node.children:
                node.children[word[i]]  = TrieNode()
            node = node.children[word[i]]
        node.end = True

class Solution:
    # @param {character[][]} board
    # @param {string[]} words
    # @return {string[]}
    def findWords(self, board, words):
        self.res = set()
        trie = TrieNode()
        for w in words:
            trie.insert(w)
        
        m = len(board)
        n = len(board[0])
        visited = [[False]*n for i in range(m)]
        
        for i in range(m):
            for j in range(n):
                self.dfs(i, j, "", board, visited, trie)
        return list(self.res)
    
    def dfs(self, i, j, word, board, visited, trie):
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or visited[i][j]:
            return
        
        if board[i][j] not in trie.children:
            return
        
        if trie.children[board[i][j]].end:
            self.res.add(word + board[i][j])
        
        visited[i][j] = True
        self.dfs(i-1, j, word+board[i][j], board, visited, trie.children[board[i][j]])
        self.dfs(i+1, j, word+board[i][j], board, visited, trie.children[board[i][j]])
        self.dfs(i, j-1, word+board[i][j], board, visited, trie.children[board[i][j]])
        self.dfs(i, j+1, word+board[i][j], board, visited, trie.children[board[i][j]])
        visited[i][j] = False