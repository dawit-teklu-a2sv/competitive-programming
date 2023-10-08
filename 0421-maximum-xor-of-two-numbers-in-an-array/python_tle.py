class TrieNode:
    def __init__(self):
        self.next = [None, None]

class Trie:
    def __init__(self,length):
        self.root = TrieNode()
        self.length  = length
    def insert(self, num):
        curr = self.root
        for i in range(self.length-1, -1, -1):
            bit = (num >> i) & 1
            if not curr.next[bit]:
                curr.next[bit] = TrieNode()
            curr = curr.next[bit]
    
    def max_xor(self, num):
        curr = self.root
        ans = 0
        for i in range(self.length-1, -1, -1):
            bit = (num >> i) & 1
            if curr.next[1 - bit]:  # toggle bit
                ans += (1 << i)
                curr = curr.next[1 - bit]
            else:
                curr = curr.next[bit]
        return ans

class Solution:
    def findMaximumXOR(self, nums):
        length = max(nums).bit_length()
        max_ans = 0
        t = Trie(length)
        for num in nums:
            t.insert(num)
            max_ans = max(max_ans, t.max_xor(num))
        return max_ans
