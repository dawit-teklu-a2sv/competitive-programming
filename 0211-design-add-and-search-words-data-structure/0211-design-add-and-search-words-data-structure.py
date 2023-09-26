class TrieNode:
    def __init__(self):
        self.is_last = False
        self.children = [None for _ in range(26)]
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        
        for c in word:
            index = ord(c) - ord('a')
            if not curr.children[index]:
                curr.children[index] = TrieNode()
            curr = curr.children[index]
        curr.is_last = True

    def search(self, word: str) -> bool:
        def dfs(i,root):
            curr = root
            for j in range(i,len(word)):
                
                if word[j] != '.':
                    index = ord(word[j]) - ord('a')
                    
                    if not curr.children[index]:
                        return False
                    curr = curr.children[index]
                else:
                    for child in curr.children:
                        if child and dfs(j+1,child):
                            return True
                    return False
            return curr.is_last
        
        return dfs(0,self.root)
        
                    
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)