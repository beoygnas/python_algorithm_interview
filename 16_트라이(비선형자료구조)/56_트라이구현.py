# https://leetcode.com/problems/implement-trie-prefix-tree/
# 0. dict로 구현, 시간복잡도/공간복잡도 신경 안씀
import collections 

class Trie:
    
    def __init__(self):
        self.trie = None
        self.trie = collections.defaultdict(list)

    def insert(self, word: str) -> None:
        for n in range(len(word)) : 
            self.trie[word[:n+1]].append(word)

    def search(self, word: str) -> bool:
        if word in self.trie and word in self.trie[word] : 
            return True
        return False
        
    def startsWith(self, prefix: str) -> bool:
        if prefix in self.trie :
            return True
        
# 1. 트라이로 개선된 형태, 트라이를 통해 dict에서의 불필요한 key mapping은 최소화할 수 있음.
class TrieNode:
    def __init__(self):
        self.word = False
        self.children = collections.defaultdict(TrieNode)

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word : 
            node = node.children[char]
        node.word = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word : 
            if char not in node.children : 
                return False
            node = node.children[char]
        return node.word
        
    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix : 
            if char not in node.children : 
                return False
            node = node.children[char]
        return True
        