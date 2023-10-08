#Using trie 
class Solution:
    def longestWord(self, words: List[str]) -> str:
        
        words_set = set(words)
        ans = ""
        
        for word in words:
            if len(word) > len(ans) or len(word) == len(ans) and word < ans:
                if(all(word[:i] in words_set for i in range(1,len(word)))):
                    ans = word
        return ans

class Node:
    
    def __init__(self):
        self.children = {}
        self.isEnd = False
        
class Trie:
    
    def __init__(self):
        self.root = Node()
        
    def insert(self,word:str):
        root = self.root 
        
        for ch in word:
            if ch not in root.children:
                root.children[ch] = Node()
            root = root.children[ch]
        root.isEnd = True
    def checkAllPrefixes(self,word):
        root = self.root 
        for ch in word:
            if ch in root.children:
                root = root.children[ch]
                if not root.isEnd:
                    return False
            else:
                return False 
        return True
class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        for word in words:
            trie.insert(word)
        ans = ""
        
        for word in words:
            if trie.checkAllPrefixes(word):
                if len(word) > len(ans):
                    ans = word
                elif len(word) == len(ans) and word < ans:
                    ans = word 
        return ans
            
        
        
    
