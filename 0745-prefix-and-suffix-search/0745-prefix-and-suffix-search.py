class Node:
    
    def __init__(self):
        self.children = {}
        self.indexes = []
    
class TrieNode:
    
    def __init__(self):
        
        self.root = Node()
        
    def insert(self,word,index):
        root = self.root 
        
        for ch in word:
            if ch not in root.children:
                root.children[ch] = Node()
            root = root.children[ch]
            root.indexes.append(index)
    def startsWith(self,pref):
        
        root = self.root
        
        for ch in pref:
            
            if ch not in root.children:
                return []
            root = root.children[ch]
        
        return root.indexes
    

class WordFilter:

    def __init__(self, words: List[str]):
        self.words = words
        self.preTrie = TrieNode()
        self.sufTrie = TrieNode()
        
        for index,word in enumerate(words):
            self.preTrie.insert(word,index)
            self.sufTrie.insert(word[::-1],index)
    
    def f(self, pref: str, suff: str) -> int:
        prefSet = self.preTrie.startsWith(pref)
        sufSet = self.sufTrie.startsWith(suff[::-1])
        i = len(prefSet)-1
        j = len(sufSet)-1
        
        while i >= 0 and j >= 0:
            if prefSet[i] == sufSet[j]:
                return prefSet[i]
            elif prefSet[i] > sufSet[j]:
                i -= 1
            else:
                j -= 1
        return -1
        res = prefSet.intersection(sufSet)
        
        if not len(res):
            return -1
        return max(res)
      
            

        
        
        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)