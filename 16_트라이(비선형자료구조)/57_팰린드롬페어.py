# https://leetcode.com/problems/palindrome-pairs/description/

import collections

class TrieNode:
    def __init__(self):
        self.w = -1
        self.p = []
        self.children = collections.defaultdict(TrieNode)

class Trie:
    def __init__(self):
        self.root = TrieNode()

    @staticmethod
    def is_palindrome(word: str) -> bool :
        return word[::] == word[::-1]

    def insert(self, index, word: str) -> None:
        node = self.root
        for i, char in enumerate(word[::-1]) : 
            if self.is_palindrome(word[0:len(word) - i]) :
                node.p.append(index)
            node = node.children[char]
        node.w = index

    def search(self, index, word: str) -> List[List[int]]:
        result = []
        node = self.root

        while word : 
            if node.w >= 0 :
                if self.is_palindrome(word) : 
                    result.append([index, node.w])
            if not word[0] in node.children : 
                return result
            node = node.children[word[0]]
            word = word[1:]

        if node.w >= 0 and node.w != index :
            result.append([index, node.w])
        
        for p in node.p : 
            result.append([index, p])
        
        return result
        

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        
        trie = Trie()
        
        for i, word in enumerate(words) : 
            trie.insert(i, word)

        results = []

        for i, word in enumerate(words) : 
            results.extend(trie.search(i, word))

        return results
            
