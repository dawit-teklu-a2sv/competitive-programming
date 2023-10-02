class TrieNode:
    
    def __init__(self):
        self.score = 0
        self.children = {}

class MapSum:

    def __init__(self):
        self.root = TrieNode()
        self.map = {}
    def insert(self, key: str, val: int) -> None:
        root = self.root
        temp = val - self.map.get(key,0)
        self.map[key] = val 
        root.score += temp
        for ch in key:
            # root.children[ch] = TrieNode()
            # root = root.children[ch]
            root = root.children.setdefault(ch,TrieNode())
            root.score  += temp
            
                
    def sum(self, prefix: str) -> int:
        root = self.root
        for pre in prefix:
            if pre not in root.children:
                return 0
            root = root.children[pre]
        return root.score
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)