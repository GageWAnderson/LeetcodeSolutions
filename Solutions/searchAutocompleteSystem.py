import heapq

class Compare:
    """
    Compare Classes are the Pythonic way to have custom comparators in
    Heaps -> Very useful for tracking nlargest, smallest etc.
    """
    def __init__(self, hot_degree, sentence):
        self.hot_degree = hot_degree
        self.sentence = sentence
    
    def __lt__(self, other):
        if self.hot_degree == other.hot_degree:
            return self.sentence > other.sentence
        else:
            return self.hot_degree < other.hot_degree

class TrieNode:

    def __init__(self, value=None):
        self.children = dict()
        self.hot_degree = 0
        self.value = value
        self.word = None # Store whole sentence at Leaf Nodes
    
    def __str__(self):
        return f"value = {self.value}, word = {self.word}, hot_degree = {self.hot_degree}"

class Trie:

    def __init__(self):
        self.root = TrieNode()
    
    def _compare_hot_words(self, elem):
        return (elem[0], [ord(c) for c in elem[1]])
    
    def add(self, word, hot_degree):
        cur = self.root
        for letter in word:
            if letter not in cur.children:
                new_node = TrieNode(letter)
                cur.children[letter] = new_node
            cur = cur.children[letter]
        cur.hot_degree = hot_degree # Increment Hot degree for '#' at end of sentence
        cur.word = word
    
    def hot_words_with_prefix(self, prefix, n):
        cur = self.root
        for letter in prefix:
            if letter not in cur.children:
                return [] # Prefix not in Trie, no hot sentences with it
            cur = cur.children[letter]
        
        # cur is the last letter in Prefix, use a heap to track hottest sentences
        # That we find in the inorder traversal of the Trie
        hot_sentences_heap = []
        def dfs(node):
            if node.word is not None: # End of sentence
                heapq.heappush(hot_sentences_heap, Compare(node.hot_degree, node.word))
            
            for child in node.children.keys():
                dfs(node.children[child])
        dfs(cur)
        return [node.sentence for node in heapq.nlargest(n, hot_sentences_heap)]

class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.trie = Trie()
        self.NUM_HOT_WORDS = 3
        self.curr_sentence = [] # String Buffer
        for i,sentence in enumerate(sentences):
            self.trie.add(sentence, times[i])

    def input(self, c: str) -> List[str]:
        if c == "#":
            self.trie.add("".join(self.curr_sentence), 1)
            self.curr_sentence = []
            return []
        else:
            self.curr_sentence.append(c)
            return self.trie.hot_words_with_prefix("".join(self.curr_sentence), self.NUM_HOT_WORDS)

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)