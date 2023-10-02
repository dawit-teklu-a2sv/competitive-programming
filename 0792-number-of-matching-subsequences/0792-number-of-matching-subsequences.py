class TrieNode:
    
    def __init__(self,data=None):
        self.children = {}
        self.count = 0
        self.end = False
        self.data = data
        
class Trie:
    
    def __repr__(self):
        def recur(node,indent):
            return "".join(indent + key + ("$" if child.end else "") + recur(child,indent + " ") for key,child in node.children.items())
        return recur(self.root,"\n")
        
    
    
    def __init__(self):
        self.root = TrieNode()
            
    def insert(self,word):
        
        root = self.root
        
        for ch in word:
            if ch not in root.children:
                root.children[ch] = TrieNode(ch)
            root = root.children[ch]
        root.count += 1
        root.end = True

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        
        trie = Trie()
        root = trie.root
        for word in words:
            trie.insert(word)
            
        print(trie)
        def findIndex(i,ch):
            for j in range(i,len(s)):
                if s[j] == ch:
                    return j 
            return -1 
        
        def solve(node,index):
            nonlocal ans
            if node.end:
                print("count",node.count,node.data)
                ans += node.count
            
            for ch in node.children:
                i = findIndex(index + 1, ch)
                if i != -1:
                    solve(node.children[ch],i)
        ans = 0
        solve(trie.root,-1)
        return ans
        
     
        