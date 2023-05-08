class TrieNode:
    def __init__(self):
        self.children = {}
        self. endOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endOfWord = True
    
    
    def search(self, word):
        curr = self.root

        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.endOfWord
    
    def startsWith(self, prefix):
        curr = self.root

        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m,n = len(board), len(board[0])
        res = set()
        seen = set() # Set of seen coordinates

        wordsTrie = Trie()
        for word in words:
            wordsTrie.insert(word)
        
        def getNbors(row, col):
            nbors = []
            if col > 0:
                nbors.append((row, col - 1))
            if col < n - 1:
                nbors.append((row, col + 1))
            if row > 0:
                nbors.append((row - 1, col))
            if row < m - 1:
                nbors.append((row + 1, col))
            return nbors
        
        def dfs(node, currLetters, row, col):
            if not wordsTrie.startsWith(currLetters):
                return
            
            if wordsTrie.search(currLetters):
                if currLetters not in res:
                    res.add(currLetters)
                    wordsTrie.remove(currLetters) # Words are unique, so remove it after adding
                # Keep searching after appending word, there may be more letters after it
                # For example, 'app' is a prefix of the word 'apple'
            
            seen.add((row, col))
            for nbor in getNbors(row, col):
                nborRow, nborCol = nbor[0], nbor[1]
                if nbor not in seen:
                    dfs(currLetters + board[nborRow][nborCol], nborRow, nborCol)
            seen.remove((row, col))
        
        for row in range(m):
            for col in range(n):
                dfs(board[row][col], row, col)
        return list(res)