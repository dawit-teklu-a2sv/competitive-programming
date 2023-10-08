class Node:
    
    def __init__(self):
        self.children = {}
        self.count = 0
        
class TrieNode:
    
    def __init__(self):
        self.root = Node()
    
    
    def insert(self,word):
        
        root = self.root 
        
        for ch in word:
            if not ch in root.children:
                root.children[ch] = Node()
            root.children[ch].count += 1
            root = root.children[ch]
            
    def getCount(self,word):
        root = self.root 
        count = 0
        for ch in word:
            count += root.children[ch].count
            
            root = root.children[ch]
        return count
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        answer  = []
        trie = TrieNode()
        for word in words:
            trie.insert(word)
        for word in words:
            count = trie.getCount(word)
            answer.append(count)
        return answer
        
        